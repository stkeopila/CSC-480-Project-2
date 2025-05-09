import sys
import math
import random


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
    if answer == "Fold" or "fold":
        print("Game Over")
    elif answer == "Stay" or "stay":
        print("Stay")
    else:
        ("Can Only Choose Fold or Stay")

def pre_flop(deck):
    bot, player = [], []
    for i in range(2):
        playerCard = random.choice(deck)
        player.append(playerCard)
        deck.remove(playerCard)
        botCard = random.choice(deck)
        bot.append(botCard)
        deck.remove(botCard)
    print(f"Bot: {bot}\nPlayer: {player}")
    return(bot, player)


if __name__ == "__main__":
    deck = initialize_deck()
    start_game(deck)