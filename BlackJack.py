import random

# ... (Deck, card value, and dealing functions) ...

def play_blackjack():
    # ... (Initialize hands, deal initial cards) ...

    player_turn = True
    while player_turn:
        # ... (Display hands, ask for hit/stand) ...
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            # ... (Deal card to player, check for bust) ...
        elif choice == 's':
            player_turn = False

    # ... (Dealer's turn) ...
    # ... (Determine winner) ...

# Call play_blackjack() to start the game