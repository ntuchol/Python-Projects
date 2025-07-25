import os

def list_directory_contents(directory_path):
    try:
        # Get the list of files and directories
        entries = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for entry in entries:
            full_path = os.path.join(directory_path, entry)
            if os.path.isdir(full_path):
                print(f"[DIR]  {entry}")
            else:
                print(f"[FILE] {entry}")
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path to list: ")
    list_directory_contents(directory)
