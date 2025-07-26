    import inflect
    p = inflect.engine()
    word = "book"
    plural_word = p.plural(word)
    print(f"The plural of {word} is {plural_word}") 

    word = "child"
    plural_word = p.plural(word)
    print(f"The plural of {word} is {plural_word}") 
