import random
print random.randrange(1,6)
print "Would you like to roll the dice again?"
answer = raw_input("Please type yes or no:" ) 

while answer != "yes" and answer != "no":
    print("Try again") 
    answer = raw_input("Please type yes or no:") 

if answer == "yes":
    print random.randrange(1,6)

