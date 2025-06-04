    import inflect
    p = inflect.engine()
    word = "book"
    plural_word = p.plural(word)
    print(f"The plural of {word} is {plural_word}") # Output: The plural of book is books

    word = "child"
    plural_word = p.plural(word)
    print(f"The plural of {word} is {plural_word}") # Output: The plural of child is children