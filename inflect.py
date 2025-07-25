import inflect

def number_to_words():
    p = inflect.engine()
    
    try:
        user_input = int(input("Enter an integer: "))
        
        words = p.number_to_words(user_input)
        
        print(f"The number {user_input} in words is: {words}")
    except ValueError:
        print("Please enter a valid integer.")

number_to_words()
