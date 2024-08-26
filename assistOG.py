# import subprocess
# import sys
# import os
# from dotenv import load_dotenv
# from groq import Groq


# def find_virtualenv(path):
#     possible_dirs = ['venv', '.venv', 'env']
#     for directory in possible_dirs:
#         env_path = os.path.join(path, directory)
#         if os.path.isdir(env_path):
#             return env_path
#     return None

# def activate_virtualenv(venv_path):
#     if os.name == 'nt':  # Windows
#         activate_script = os.path.join(venv_path, 'Scripts', 'activate')
#         return f'{activate_script} && '
#     else:  # Unix-based (Linux, macOS)
#         activate_script = os.path.join(venv_path, 'bin', 'activate')
#         return f'source {activate_script} && '
    
# def run_code_file(file_path):
#     global errorMessage  # Declare errorMessage as global
#     errorMessage = None  # Initialize errorMessage to None

#     base_dir = os.path.dirname(file_path)
#     venv_path = find_virtualenv(base_dir)
#     if not venv_path:
#         # Check the parent directory
#         parent_dir = os.path.abspath(os.path.join(base_dir, os.pardir))
#         venv_path = find_virtualenv(parent_dir)
    
#     if (venv_path):
#         print("Virtual environment exists.")
#         activation_command = activate_virtualenv(venv_path)
#         run_command = f'{activation_command}python {file_path}'
#         print("Virtual environment activated.")
#     else:
#         print("No virtual environment detected.")
#         run_command = f'python {file_path}'

#     try:
#         # Run the code file and capture the output
#         result = subprocess.run(
#             run_command,
#             shell=True,
#             capture_output=True,
#             text=True,
#             check=True
#         )
#         print("Output of the code file:")
#         print(result.stdout)
#     except subprocess.CalledProcessError as e:
#         print("Output of the code file:")
#         errorMessage = e.stderr  # Assign to global errorMessage
#         print(e.stderr)
#     except FileNotFoundError:
#         print("File not found. Please check the file path.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

#     # Present options after displaying output
#     while True:
#         print("\nOptions:")
#         print("1. Exit the program")
#         print("2. Assist")
#         choice = input("Enter your choice: ").strip()

#         if choice == '1':
#             print("Exit the program selected.")
#             sys.exit()
#         elif choice == '2':
#             print("Assist selected.")
#             display_code(file_path)
#             rectified_code = get_rectified_code()
#             print("RECTIFIED CODE")
#             print(rectified_code)
#             break
#         else:
#             print("Invalid choice. Please enter 1 or 2.")


# def display_code(file_path):
#     global existing_code
#     existing_code=None
#     try:
#         with open(file_path, 'r') as file:
#             existing_code = file.read()
#         print("\nExisting code:")
#         print(existing_code)

#     except FileNotFoundError:
#         print("The specified file was not found.")
#     except Exception as e:
#         print(f"An error occurred while reading the file: {e}")





# def get_rectified_code():
#     # Load environment variables from .env file
#     load_dotenv()
#     # Initialize the Groq client
#     client = Groq(
#         api_key=os.environ.get("GROQ_API_KEY"),
#     )


#     # Example usage
#     system_prompt = "You are a python expert"
#     user_prompt = "provide rectified code"
#     # existing_code_prompt = """
#     # print("Error code")

#     # # Intentional mistake: missing parentheses
#     # print"This will cause an error"
#     # """
        

#     existing_code_prompt = f"""
#     This is the existing code:
#     {existing_code}
#     """

#     error_prompt = f"""
#     The code produced the following error:
#     {errorMessage}
#     """

#     instruction_for_response_prompt = "Provide only the rectified code nothing else"

#     # Create the chat completion request with multiple prompts
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": user_prompt},
#             {"role": "user", "content": existing_code_prompt},
#             {"role": "user", "content": error_prompt},
#             {"role": "user", "content": instruction_for_response_prompt},
#         ],
#         model="llama3-8b-8192",
#     )

#     # Return the rectified code
#     return chat_completion.choices[0].message.content



# if __name__ == "__main__":
#     if len(sys.argv) != 1:
#         print("Usage: python app.py")
#     else:
#         target_file = input("Enter the path of the target file: ").strip()
#         run_code_file(target_file)






import subprocess
import sys
import os
from dotenv import load_dotenv
from groq import Groq


def find_virtualenv(path):
    possible_dirs = ['venv', '.venv', 'env']
    for directory in possible_dirs:
        env_path = os.path.join(path, directory)
        if os.path.isdir(env_path):
            return env_path
    return None

def activate_virtualenv(venv_path):
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_path, 'Scripts', 'activate')
        return f'{activate_script} && '
    else:  # Unix-based (Linux, macOS)
        activate_script = os.path.join(venv_path, 'bin', 'activate')
        return f'source {activate_script} && '
    
def run_code_file(file_path):
    error_message = None  # Initialize error_message to None

    base_dir = os.path.dirname(file_path)
    venv_path = find_virtualenv(base_dir)
    if not venv_path:
        # Check the parent directory
        parent_dir = os.path.abspath(os.path.join(base_dir, os.pardir))
        venv_path = find_virtualenv(parent_dir)
    
    if venv_path:
        print("Virtual environment exists.")
        activation_command = activate_virtualenv(venv_path)
        run_command = f'{activation_command}python {file_path}'
        print("Virtual environment activated.")
    else:
        print("No virtual environment detected.")
        run_command = f'python {file_path}'

    try:
        # Run the code file and capture the output
        result = subprocess.run(
            run_command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        print("Output of the code file:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Output of the code file:")
        error_message = e.stderr  # Assign to error_message
        print(e.stderr)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Present options after displaying output
    while True:
        print("\nOptions:")
        print("1. Exit the program")
        print("2. Assist")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("Exit the program selected.")
            sys.exit()
        elif choice == '2':
            print("Assist selected.")
            existing_code = display_code(file_path)
            rectified_code = get_rectified_code(existing_code, error_message)
            print("RECTIFIED CODE")
            print(rectified_code)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


def display_code(file_path):
    existing_code = None
    try:
        with open(file_path, 'r') as file:
            existing_code = file.read()
        print("\nExisting code:")
        print(existing_code)

    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    
    return existing_code


def get_rectified_code(existing_code, error_message):
    # Load environment variables from .env file
    load_dotenv()

    # Initialize the Groq client
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # Example usage
    system_prompt = "You are a python expert"
    user_prompt = "provide rectified code"

    existing_code_prompt = f"""
    This is the existing code:
    {existing_code}
    """
    print(existing_code_prompt)

    error_prompt = f"""
    The code produced the following error:
    {error_message}
    """
    print(error_message)
    instruction_for_response_prompt = "Provide only the rectified code nothing else"

    # Create the chat completion request with multiple prompts
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
            {"role": "user", "content": existing_code_prompt},
            {"role": "user", "content": error_prompt},
            {"role": "user", "content": instruction_for_response_prompt},
        ],
        model="llama3-8b-8192",
    )

    # Return the rectified code
    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python app.py")
    else:
        target_file = input("Enter the path of the target file: ").strip()
        run_code_file(target_file)





