# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:09:29 2016

@author: Natalia Tucholska
"""
import pygame 
import random

pygame.init()
BLACK = ( 0, 0, 0) 
WHITE = (255, 255, 255)
word_list = ("bangle", "crow", "giant", "rainbow", "longitude")
word = random.choice(word_list)


size = [300,300]
screen = pygame.display.set_mode(size)

background = pygame.Surface(screen.get_size())
background.fill(WHITE) 
screen.blit(background, (0, 0))

pygame.draw.line(screen, BLACK,  (100, 200), (150,200), 5)
pygame.draw.line(screen, BLACK,  (125, 200), (125,50), 5)
pygame.draw.line(screen, BLACK,  (125, 50), (175,50), 5)
pygame.draw.line(screen, BLACK,  (175, 50), (175,75), 5)

pygame.display.update()
done = False
clock = pygame.time.Clock()



print("Welcome to Hangman!")

def draw_hangman(counter):
    if counter == 6:
        print("Ops that's incorrect.")
        pygame.display.update(pygame.draw.circle(screen, BLACK, [175, 75], 13))
        print("You have 5 guesses left.")
    elif counter == 5: 
        print("Ops that's incorrect.")
        pygame.display.update(pygame.draw.line(screen, BLACK, [175, 75],[175, 150], 5))
        print("You have 4 guesses left.")
    elif  counter == 4:
        print("Ops that's incorrect.")
        pygame.display.update(pygame.draw.line(screen, BLACK, [175, 110],[200, 90], 5))
        print("You have 3 guesses left.")
    elif counter == 3:
        print("Ops that's incorrect.") 
        pygame.display.update(pygame.draw.line(screen, BLACK, [175, 110],[150, 90], 5))
        print("You have 2 guesses left.")
    elif counter == 2:
        print("Ops that's incorrect.")
        pygame.display.update(pygame.draw.line(screen, BLACK, [175, 150],[200, 175], 5))
        print("You have 1 guess left.")
    elif counter == 1:
        print("Ops that's incorrect.")
        pygame.display.update(pygame.draw.line(screen, BLACK, [175, 150],[150, 175], 5))
        print("Game Over, YOU LOSE.")
        print("The word was " + word)


def is_letter_in_word(guess, letters_found): 
    for letter in word:
        if letter == guess:
            print("Congrats! You found letter " + str(word.index(letter) + 1) + " of " + str(len(word)))
            return True
    return False

counter = 6 
letters_found = 0


if letters_found == len(word):
    print("Great Job, YOU WON.")
    
while letters_found < len(word) and counter > 0: 
    print("The mystery word has " + str(len(word)) + " letters")
    guess = input("Please guess a letter from a-z:")
    found = is_letter_in_word(guess, letters_found)
    if found == True:
        letters_found = letters_found + 1 
    if found == False:
        draw_hangman(counter)
        counter = counter - 1

while not done:
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

pygame.quit()

