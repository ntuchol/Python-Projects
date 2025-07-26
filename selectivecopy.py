import os
import shutil

def selective_copy(src_dir, dest_dir, file_extension):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(src_dir):
        src_file = os.path.join(src_dir, item)
        
        if os.path.isfile(src_file) and src_file.endswith(file_extension):
            dest_file = os.path.join(dest_dir, item)
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {src_file} to {dest_file}")

source_directory = '/path/to/source'
destination_directory = '/path/to/destination'
file_ext = '.txt'

selective_copy(source_directory, destination_directory, file_ext)
