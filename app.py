import subprocess
import sys
import os

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
        print(e.stderr)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python app.py")
    else:
        target_file = input("Enter the path of the target file: ").strip()
        run_code_file(target_file)


