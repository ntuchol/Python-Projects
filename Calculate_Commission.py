def calculate_commission(car_type, sales_profit):
    if car_type == "new":
        commission_rate = 0.035  
    elif car_type == "used":
        commission_rate = 0.025  
    else:
        return "Invalid car type"

    commission = sales_profit * commission_rate
    return commission

def main():
    car_type = input("Enter car type (new/used): ").lower()
    try:
        sales_profit = float(input("Enter sales profit: "))
    except ValueError:
        print("Invalid input for sales profit.")
        return

    commission = calculate_commission(car_type, sales_profit)

    if isinstance(commission, str):
         print(commission)
    else:
        print(f"The commission is: ${commission:.2f}")

if __name__ == "__main__":
    main()

import random

def get_fortune():
    fortunes = [
        "You will have a pleasant surprise soon.",
        "The early bird gets the worm, but the second mouse gets the cheese.",
        "A journey of a thousand miles begins with a single step.",
        "Don't count your chickens before they hatch.",
        "The fortune you seek is in another cookie.",
        "You will find happiness in unexpected places.",
        "A smile is your passport into the hearts of others.",
        "Your hard work will pay off soon.",
        "The best is yet to come.",
        "Believe in yourself and anything is possible."
    ]
    return random.choice(fortunes)

def main():
    input("Press Enter to open your fortune cookie...")
    print("Your fortune:", get_fortune())

if __name__ == "__main__":
    main()

import random

def coin_flip(num_flips):
    for _ in range(num_flips):
        result = random.choice(["Heads", "Tails"])
        print(result)

coin_flip(100)

import random

def deal_card(deck):
    return deck.pop()

def calculate_hand_value(hand):
    ace_count = hand.count('A')
    total = 0
    for card in hand:
        if card.isdigit():
            total += int(card)
        elif card in ('J', 'Q', 'K'):
            total += 10
        elif card == 'A':
            total += 11
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def display_hands(player_hand, dealer_hand, hide_dealer=True):
    print(f"Player's hand: {player_hand} ({calculate_hand_value(player_hand)})")
    if hide_dealer:
        print(f"Dealer's hand: [Hidden], {dealer_hand[1:]} ")
    else:
        print(f"Dealer's hand: {dealer_hand} ({calculate_hand_value(dealer_hand)})")

def play_blackjack():
    deck = [str(i) for i in range(2, 11)] * 4 + ['J'] * 4 + ['Q'] * 4 + ['K'] * 4 + ['A'] * 4
    random.shuffle(deck)
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    display_hands(player_hand, dealer_hand)
    while True:
        action = input("Hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deal_card(deck))
            display_hands(player_hand, dealer_hand)
            if calculate_hand_value(player_hand) > 21:
                print("Bust! You lose.")
                break
        elif action == 's':
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deal_card(deck))
            display_hands(player_hand, dealer_hand, hide_dealer=False)
            if calculate_hand_value(dealer_hand) > 21 or calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
                print("You win!")
            elif calculate_hand_value(player_hand) == calculate_hand_value(dealer_hand):
                 print("It's a push!")
            else:
                print("You lose.")
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

if __name__ == "__main__":
    play_blackjack()

import tkinter as tk
root = tk.Tk()
root.title("Order Up Program")
label = tk.Label(root, text="Select your items:")
label.pack()

item1_var = tk.IntVar()
item1_check = tk.Checkbutton(root, text="Pizza", variable=item1_var)
item1_check.pack()

item2_var = tk.IntVar()
item2_check
