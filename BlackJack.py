import random

def play_blackjack():

    player_turn = True
    while player_turn:
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
        elif choice == 's':
            player_turn = False
