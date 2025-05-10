import sys
import random
import time
from collections import Counter

def hand_value(hand, cards_on_table):
    hand_rankings = {"Royal Flush": 23, "Straight Flush":22, "Four of a Kind":21, "Full House":20, "Flush":19, "Straight":18, "Three of a Kind":17, "Two Pair":16, "One Pair":15, "High Card":1 }
    current_hand = hand + cards_on_table
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

    if flush_card and set([10, 11, 12, 13, 14]).issubset(set(flush_card)):
        return hand_rankings["Royal Flush"]
    
    elif flush and straight == True:
        return hand_rankings["Straight Flush"]

    elif 4 in value_counts.values():
        return hand_rankings["Four of a Kind"]

    elif 3 in value_counts.values() and 2 in value_counts.values():
        return hand_rankings["Full House"]

    elif flush:
        return hand_rankings["Flush"]
    
    elif straight:
        return hand_rankings["Straight"]

    elif 3 in value_counts.values():
        return hand_rankings["Three of a Kind"]

    elif list(value_counts.values()).count(2) >= 2:
        return hand_rankings["Two Pair"]
    
    elif 2 in value_counts.values():
        return hand_rankings["One Pair"]

    else:
        curr_hand = [card[2] for card in current_hand]
        high_card = max(curr_hand)
        return high_card

def monte_carlo_search(hand, cards_on_table, deck):
    wins, simulations = 0, 0
    time_limit = 10
    time_start = time.time()
    while time.time() - time_start < time_limit:
        available_cards = [card for card in deck if card not in hand + cards_on_table]
        ran_player_hand = random.sample(available_cards, 2)
        for card in ran_player_hand:
            available_cards.remove(card)
        needed = 5 - len(cards_on_table)
        random_sim = cards_on_table + random.sample(available_cards, needed)
        bot_score = hand_value(hand, random_sim)
        player_score = hand_value(ran_player_hand, random_sim)
        if bot_score >= player_score:
            wins += 1
        simulations += 1
    wr = wins / simulations
    print(f"Simulations: {simulations}")
    print(f"Wins: {wins}")
    print(f"Ratio: {wr}")

    if wr >= 0.5:
        return "Stay"
    else:
        return "Fold"
    

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
    available_cards = deck
    cards_on_table = []
    bot, player, available_cards = pre_flop(deck)
    if monte_carlo_search(bot, cards_on_table, deck) == "Fold":
        print("Folded On Pre Flop")
        sys.exit(1)
    cards_on_table = flop(available_cards)
    if monte_carlo_search(bot, cards_on_table, deck) == "Fold":
        print("Folded On Flop")
        sys.exit(1)
    cards_on_table = cards_on_table + turn(available_cards)
    if monte_carlo_search(bot, cards_on_table, deck) == "Fold":
        print("Folded On Turn")
        sys.exit(1)
    cards_on_table = cards_on_table + river(available_cards)
    if monte_carlo_search(bot, cards_on_table, deck) == "Fold":
        print("Folded On River")
        sys.exit(1)
    if hand_value(bot, cards_on_table) > hand_value(player, cards_on_table):
        print("win")
        print(f"Bot Hand: {bot}")
        print(f"Player Hand: {player}")
        print(f"Cards on Table: {cards_on_table}")
    else:
        print("loss")
        print(f"Bot Hand: {bot}")
        print(f"Player Hand: {player}")
        print(f"Cards on Table: {cards_on_table}")

def river(deck):
    card_river = random.sample(deck, 1)[0]
    deck.remove(card_river)
    return [card_river]

def turn(deck):
    card_turned = random.sample(deck, 1)[0]
    deck.remove(card_turned)
    return [card_turned]

def flop(deck):
    cards_on_table = random.sample(deck, 3)
    for card in cards_on_table:
        deck.remove(card)
    return cards_on_table

def pre_flop(deck):
    bot = random.sample(deck, 2)
    for card in bot:
        deck.remove(card)
    player = random.sample(deck, 2)
    for card in player:
        deck.remove(card)
    return(bot, player, deck)


if __name__ == "__main__":
    deck = initialize_deck()
    start_game(deck)