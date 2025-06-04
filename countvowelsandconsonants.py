def count_vowels_and_consonants():
    # Prompt the user for input
    user_input = input("Enter a string: ").lower()

    # Define vowels
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    # Iterate through the string
    for char in user_input:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    # Display the results
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")

# Call the function
count_vowels_and_consonants()