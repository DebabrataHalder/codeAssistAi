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
