import random

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card_rank, _ in hand:
        if card_rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif card_rank == 'Ace':
            num_aces += 1
            value += 11  # Assume 11 initially
        else:
            value += int(card_rank)

    while value > 21 and num_aces > 0:
        value -= 10  # Change Ace from 11 to 1
        num_aces -= 1
    return value


while player_total < 21:
    action = input("Do you want to hit or stand? (H/S): ").upper()
    if action == 'H':
        player_hand.append(deck.pop())
        player_total = calculate_hand_value(player_hand)
    elif action == 'S':
        break
    else:
        print("Invalid input. Please enter 'H' or 'S'.")

