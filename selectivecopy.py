import os
import shutil

def selective_copy(src_dir, dest_dir, file_extension):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over all files in the source directory
    for item in os.listdir(src_dir):
        # Construct full file path
        src_file = os.path.join(src_dir, item)
        
        # Check if it's a file and has the desired extension
        if os.path.isfile(src_file) and src_file.endswith(file_extension):
            # Construct the destination file path
            dest_file = os.path.join(dest_dir, item)
            # Copy the file
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {src_file} to {dest_file}")

# Example usage
source_directory = '/path/to/source'
destination_directory = '/path/to/destination'
file_ext = '.txt'

selective_copy(source_directory, destination_directory, file_ext)