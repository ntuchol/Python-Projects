import random

def generate_powerball_numbers():
    # Generate 5 unique white ball numbers (1-69)
    white_balls = random.sample(range(1, 70), 5)
    # Generate the Powerball number (1-26)
    powerball = random.randint(1, 26)
    
    return white_balls, powerball

# Generate and display Powerball numbers
white_balls, powerball = generate_powerball_numbers()
print("Your Powerball numbers are:")
print(f"White Balls: {sorted(white_balls)}")
print(f"Powerball: {powerball}")