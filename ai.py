# import os
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()

# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Hi",
#         }
#     ],
#     model="llama3-8b-8192",
# )

# print(chat_completion.choices[0].message.content)





















import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client with the API key
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Create chat completion with system and user prompts
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an expert Python developer."
        },
        {
            "role": "user",
            "content": "Write code for a chess game with Python."
        }
    ],
    model="llama3-8b-8192",
)

# Print the response from the model
print(chat_completion)
