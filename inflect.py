import inflect

def number_to_words():
    # Create an inflect engine
    p = inflect.engine()
    
    try:
        # Input an integer from the user
        user_input = int(input("Enter an integer: "))
        
        # Convert the number to its written format
        words = p.number_to_words(user_input)
        
        print(f"The number {user_input} in words is: {words}")
    except ValueError:
        print("Please enter a valid integer.")

# Run the function
number_to_words()