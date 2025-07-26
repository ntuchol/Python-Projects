import random

def generate_powerball_numbers():
    white_balls = random.sample(range(1, 70), 5)
    powerball = random.randint(1, 26)
    
    return white_balls, powerball

white_balls, powerball = generate_powerball_numbers()
print("Your Powerball numbers are:")
print(f"White Balls: {sorted(white_balls)}")
print(f"Powerball: {powerball}")
