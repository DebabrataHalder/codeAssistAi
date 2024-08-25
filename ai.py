# import os
# from dotenv import load_dotenv
# from groq import Groq

# # Load environment variables from .env file
# load_dotenv()

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY"),
# )

# # Ask user to enter system prompt
# system_prompt = "Be a senior computer programmer"

# # Ask user to enter user prompt
# user_prompt = input("Enter user prompt: ")

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "system",
#             "content": system_prompt,
#         },
#         {
#             "role": "user",
#             "content": user_prompt,
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

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# Ask user to enter system prompt
system_prompt = "You are a senior computer programmer who can debug and improve code."

# Ask user to enter existing code
existing_code_prompt = input("Enter the existing code: ")

# Ask user to enter user prompt
user_prompt = input("Enter your prompt or description for the rectification: ")

# Construct the full prompt for the API request
full_prompt = f"Here is the existing code:\n{existing_code_prompt}\n\n{user_prompt}"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": full_prompt,
        }
    ],
    model="llama3-8b-8192",
)

# Print the rectified code response
print("Rectified Code:")
print(chat_completion.choices[0].message['content'])







































