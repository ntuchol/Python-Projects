# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 21:26:05 2016

@author: Natalia Tucholska
"""

import random 
print("Welcome to Adventure!")
x_coordinate = random.randrange(1,6)
y_coordinate = random.randrange(1,6)

position = (x_coordinate, y_coordinate)  

 
def persons_location():
    global location 
    if position == (1,1) or position == (1,2) or position == (2,1) or position == (2,2):
        location = "kitchen"
    elif position == (1,3) or position == (1,4) or position == (1,5) or position == (1,6):
        location = "hall"
    elif position == (2,3) or position == (2,4):
        location = "closet"
    elif position == (1,5) or position == (1,6) or position == (2,5) or position == (2,6):
        location = "bathroom"
    elif position == (3,1) or position == (3,2) or position == (4,1) or position == (5,1) or position == (4,2) or position == (5,2) or position == (3,2):  
        location ="hall"  
    elif position == (3,6) or position == (4,4) or position == (4,5) or position == (4,6) or position == (5,4) or position == (5,5) or position == (5,6):
        location = "bedroom 1"
    elif position == (6,1) or position == (6,2):
        location = "closet 2"
    elif position == (6,4) or position == (6,5) or position == (6,6): 
        location = "patio" 
    return location 

print("Your position is " + str(position) + " meaning that you are in the " + str(persons_location()))


def move_up_or_down(position):
    answer = input("Would you like to move up or down?:") 
    if  y_coordinate <= 6 and y_coordinate > 0:
            if answer == "up":
                position = (x_coordinate, y_coordinate + 1)  
                print(position)
            elif answer == "down":
                position = (x_coordinate, y_coordinate - 1)
                print(position)
    else:
        print("You hit a wall fool") 
    return position  

print("Your position is " + str(move_up_or_down(position)) + " meaning that you are in the " + str(persons_location()))  

position_2 = move_up_or_down(position)

def move_side_to_side(position_2): 
    answer = input("Would you like to move left or right?:") 
    if  y_coordinate <= 6 and y_coordinate > 0:
            if answer == "right":
                position_2 = (x_coordinate + 1, y_coordinate)
                print(position_2)
            elif answer == "left":
                position_2 = (x_coordinate - 1, y_coordinate)
                print(position_2)
    else:
        print("You hit a wall fool") 
    return position_2  

print("Your position is " + str(move_side_to_side(position_2)) + " meaning that you are in the " + str(persons_location())) 

position_3 = move_side_to_side(position_2)

def move_again(position_3): 
    answer = input("Would you like to move again?") 
    while answer == "yes":
        position_4 = move_up_or_down(position_3)
        print(position_4)
        position_5 = move_side_to_side(position_4)
        print(position_5)
        print("Your position is " + str(position_5) + " meaning that you are in the " + str(persons_location())) 
        answer = input("Would you like to move again?")        
    if answer == "no":
        print("Game Over")
        return position_5 

print("Your position is " + str(move_again(position_3)) + " meaning that you are in the " + str(persons_location()))   


