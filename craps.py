import random      
import sys

a = input("TO START THE GAME TYPE 'yes' and TO QUIT TYPE 'no'\n")
if a.lower() == "no":
    sys.exit()
else:
    print("LET'S START THE GAME")

    
a = input("welcome to the game of chance,are you ready to test your fortune ,\ndo you need instructions type (yes) or (no) \n")

if a.lower() == "yes":
    print(''' 1. player rolls two six-sided dice and adds the numbers rolled together.
              2. On this first roll, a 7 or an 11 automatically wins, and a 2, 3, or 12automatically loses, and play is over.
                 If a 4, 5, 6, 8, 9, or 10 are rolled on this first roll, that number becomes the 'point.'
              3. The player continues to roll the two dice again until one of two things happens: 
                 either they roll the 'point' again, in which case they win; or they roll a 7, in which case they lose.''')

elif a.lower() == "no":
    print("all the best, player")


def diceNumber():
  
    _ = input("press enter to roll the dice ")
    
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    
    return (die1, die2)  

def twoDice(dices):
    die1, die2 = dices
    print("player- the sum of numbers you have got in die 1 and die 2 are {} + {} = {}".format(die1, die2, sum(dices)))


value = diceNumber()
twoDice(value)

sum_of_dices = sum(value)


if sum_of_dices in (7, 11):
    result = "congratulations you won"

elif sum_of_dices in (2, 3, 12):
    result = "you lost, \ntry again next time"
else:  
    result = "continue your game please"
    currentpoint = sum_of_dices
    print("good game, your current point is", currentpoint)

while result == "continue your game please":
    value = diceNumber()
    twoDice(value)
    sum_of_dices = sum(value)
    
    if sum_of_dices == currentpoint:
        result = "congratulations you won"
        
    elif sum_of_dices == 7:
        result = "you lost,\n try again next time"

if result == "congratulations you won":
    print("congratulations,you won")
    
else:
    print("you lost, \ntry again next time")
