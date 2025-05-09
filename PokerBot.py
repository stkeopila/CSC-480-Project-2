import sys
import math
import random

# def hand_value(hand, cards_on_table):


def initialize_deck():
    suits = ['Diamond', 'Clubs', 'Heart', 'Spade']
    numbers = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    deck = []
    for suit in suits:
        for number, value in numbers.items():
            card = (number, suit, value)
            deck.append(card)
    return deck

def start_game(deck):
    removed_cards = []
    bot, player = pre_flop(deck)
    for card in bot:
        removed_cards.append(card)
    print("Fold or Stay?")
    answer = input()
    if answer.lower() == "fold":
        print("Game Over")
    elif answer.lower() == "stay":
        cards_on_table, removed_cards = flop(deck, removed_cards)
        for card, suit, value in cards_on_table:
            print(f"{card}, {suit}")
    else:
        ("Can Only Choose Fold or Stay")

def flop(deck, removed_cards):
    cards_on_table = []
    for i in range(3):
        flopCard = random.choice(deck)
        cards_on_table.append(flopCard)
        deck.remove(flopCard)
        removed_cards.append(flopCard)
    return cards_on_table, removed_cards

def pre_flop(deck):
    bot, player = [], []
    for i in range(2):
        playerCard = random.choice(deck)
        player.append(playerCard)
        deck.remove(playerCard)
        botCard = random.choice(deck)
        bot.append(botCard)
        deck.remove(botCard)
    for card, suit, value in bot:
        print(f"Bot: {card}, {suit}")
    for card, suit, value in player:
        print(f"Player: {card}, {suit}")
    return(bot, player)


if __name__ == "__main__":
    deck = initialize_deck()
    start_game(deck)