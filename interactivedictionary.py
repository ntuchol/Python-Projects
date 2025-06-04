import json
from difflib import get_close_matches

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def find_definition(word, data):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        closest_match = get_close_matches(word, data.keys())[0]
        confirmation = input(f"Did you mean {closest_match} instead? Enter Y for yes, N for no: ").upper()
        if confirmation == "Y":
            return data[closest_match]
        elif confirmation == "N":
             return "The word doesn't exist. Please double-check it."
        else:
            return "Invalid input."
    else:
        return "The word doesn't exist. Please double-check it."
    
def main():
    data = load_data('data.json')

    while True:
        user_word = input("Enter a word (or type 'exit' to quit): ")
        if user_word.lower() == 'exit':
            break
        
        definition = find_definition(user_word, data)
        
        if isinstance(definition, list):
            for entry in definition:
                print(entry)
        else:
            print(definition)

if __name__ == "__main__":
    main()