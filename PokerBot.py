import sys
import math
import random


def initialize_deck():
    suits = ['Diamond', 'Clubs', 'Heart', 'Spade']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for suit in suits:
        for number in numbers:
            card = (number, suit)
            deck.append(card)
    return deck

def start_game(deck):
    cards_out_of_deck = []
    ran_card = random.choice(deck)
    cards_out_of_deck.append(ran_card)
    print(ran_card)
    print(cards_out_of_deck)


if __name__ == "__main__":
    deck = initialize_deck()
    start_game(deck)