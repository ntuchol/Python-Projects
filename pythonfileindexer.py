import os
import json

def create_index(directory):
    index = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            index[file] = path
    return index

def save_index(index, filepath="index.json"):
    with open(filepath, "w") as f:
        json.dump(index, f, indent=4)

def load_index(filepath="index.json"):
     with open(filepath, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    index_data = create_index("path/to/your/directory")
    save_index(index_data)
    loaded_index = load_index()
    print(loaded_index)