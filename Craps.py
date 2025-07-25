import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def play_craps():
    print("Welcome to Craps!")
    
    come_out_roll = roll_dice()
    print(f"Come Out Roll: {come_out_roll}")

    if come_out_roll in (7, 11):
        print("Natural! You Win!")
    elif come_out_roll in (2, 3, 12):
        print("Craps! You Lose!")
    else:
        point = come_out_roll
        print(f"Point is: {point}")
        
        while True:
            next_roll = roll_dice()
            print(f"Next Roll: {next_roll}")
            
            if next_roll == point:
                print("Point Hit! You Win!")
                break
            elif next_roll == 7:
                print("Seven Out! You Lose!")
                break
