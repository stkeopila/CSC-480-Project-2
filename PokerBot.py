import sys
import math
import random
from collections import Counter

def hand_value(hand, cards_on_table):
    hand_rankings = {"Royal Flush": 10, "Straight Flush":9, "Four of a Kind":8, "Full House":7, "Flush":6, "Straight":5, "Three of a Kind":4, "Two Pair":3, "One Pair":2, "High Card":1 }
    current_hand = hand + cards_on_table
    print(current_hand)
    values = []
    suits = []
    for card in current_hand:
        values.append(card[2])
    values.sort(reverse=True)
    for card in current_hand:
        suits.append(card[1])
    value_counts = Counter(values)
    suit_counts = Counter(suits)
    flush = None
    for suit, count in suit_counts.items():
        if count >= 5:
            flush = suit
    flush_card = []
    if flush:
        for card in current_hand:
            if card[1] == flush:
                flush_card.append(card[2])
    straight = False
    straight_value = sorted(set(values))
    for i in range(len(straight_value) - 4):
        straight_window = straight_value[i:i+5]
        if straight_window[-1] - straight_window[0] == 4:
            straight = True
    print(flush_card)

    print(value_counts)
    print(suit_counts)

    if flush_card and set([10, 11, 12, 13, 14]).issubset(set(flush_card)):
        print("royal Flsuh")
        return hand_rankings["Royal Flush"]
    
    elif flush and straight == True:
        print("Straight Flush")
        return hand_rankings["Straight Flush"]

    elif 4 in value_counts.values():
        return hand_rankings["Four of a Kind"]

    elif 3 in value_counts.values() and 2 in value_counts.values():
        print("Full House")
        return hand_rankings["Full House"]

    elif flush:
        print("Flush")
        return hand_rankings["Flush"]
    
    elif straight:
        print("Straight")
        return hand_rankings["Straight"]

    elif 3 in value_counts.values():
        print("Three of a kind")
        return hand_rankings["Three of a Kind"]

    elif list(value_counts.values()).count(2) >= 2:
        print("Two Pair")
        return hand_rankings["Two Pair"]
    
    elif 2 in value_counts.values():
        print("One Pair")
        return hand_rankings["One Pair"]

    else:
        print("High card") 
        return hand_rankings["High Card"]



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
    cards_on_table, removed_cards = flop(deck, removed_cards)
    for card, suit, value in cards_on_table:
        print(f"{card}, {suit}")
    hand_value(bot, cards_on_table)

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