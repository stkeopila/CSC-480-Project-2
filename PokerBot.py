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
    ran_num = random.choice(deck)
    print(ran_num)


if __name__ == "__main__":
    deck = initialize_deck()
    start_game(deck)