import subprocess
import sys
import os
from components.virtualenv_utils import find_virtualenv, activate_virtualenv
from components.file_utils import display_code
from components.groq_utils import get_rectified_code

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
            user_prompt_input = input("Enter your prompt (press Enter to use default): ").strip()
            existing_code = display_code(file_path)
            rectified_code = get_rectified_code(existing_code, error_message, user_prompt_input)
            print("RECTIFIED CODE")
            print(rectified_code)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        target_file = sys.argv[1]  # Get the target file path from the command-line argument
        run_code_file(target_file)
    else:
        print("Usage: python app.py <target_file_path>")


















































# import subprocess
# import sys
# import os
# from components.virtualenv_utils import find_virtualenv, activate_virtualenv
# from components.file_utils import display_code
# from components.groq_utils import get_rectified_code

# def run_code_file(file_path):
#     error_message = None  # Initialize error_message to None

#     base_dir = os.path.dirname(file_path)
#     venv_path = find_virtualenv(base_dir)
#     if not venv_path:
#         # Check the parent directory
#         parent_dir = os.path.abspath(os.path.join(base_dir, os.pardir))
#         venv_path = find_virtualenv(parent_dir)
    
#     if venv_path:
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
#         error_message = e.stderr  # Assign to error_message
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
#             user_prompt_input = input("Enter your prompt (press Enter to use default): ").strip()
#             existing_code = display_code(file_path)
#             rectified_code = get_rectified_code(existing_code, error_message, user_prompt_input)
#             print("RECTIFIED CODE")
#             print(rectified_code)
#             break
#         else:
#             print("Invalid choice. Please enter 1 or 2.")


# if __name__ == "__main__":
#     if len(sys.argv) != 1:
#         print("Usage: python run_code.py")
#     else:
#         target_file = input("Enter the path of the target file: ").strip()
#         run_code_file(target_file)
