import random
random_number = int(random.randrange(1000))
user_guess = raw_input("What do you think this random number is?: ")

while(user_guess.isdigit() == False):
    print "Please guess a digit"
    user_guess = raw_input("What do you think this random number is?: ")
    
user_guess = int(user_guess)
if(random_number != user_guess): 
    if(random_number > user_guess):
        print "The random number is " + str(random_number) + " meaning that"
        difference = abs(user_guess - random_number)  
        print "your guess is too low,it is off by " + str(difference)
    elif(random_number < user_guess):
        print random_number
        difference = str(random_number - user_guess)
        print "your guess is too high, it is off by " + str(difference)
else:
    print "Great job! You guessed correctly."
     