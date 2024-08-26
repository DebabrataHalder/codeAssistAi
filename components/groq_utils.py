import os
from dotenv import load_dotenv
from groq import Groq

def get_rectified_code(existing_code, error_message, user_prompt_input=None):
    # Load environment variables from .env file
    load_dotenv()

    # Initialize the Groq client
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # Example usage
    system_prompt = "You are a python expert"
    user_prompt = user_prompt_input if user_prompt_input else "provide rectified code"

    existing_code_prompt = f"""
    This is the existing code:
    {existing_code}
    """

    error_prompt = f"""
    The code produced the following error:
    {error_message}
    """

    # Prepare messages based on user input
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        {"role": "user", "content": existing_code_prompt},
        {"role": "user", "content": error_prompt},
    ]

    # Only add the instruction if no custom user prompt is provided
    if not user_prompt_input:
        instruction_for_response_prompt = "Provide only the rectified code, nothing else"
        messages.append({"role": "user", "content": instruction_for_response_prompt})

    # Create the chat completion request with the prepared messages
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
    )

    # Return the rectified code
    return chat_completion.choices[0].message.content
