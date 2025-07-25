def count_vowels_and_consonants():
    user_input = input("Enter a string: ").lower()

    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for char in user_input:
        if char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")

count_vowels_and_consonants()
