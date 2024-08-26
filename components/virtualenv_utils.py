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
