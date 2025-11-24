""" Main Blackjack Game """
import random

def create_deck():
    """ Create 1 standard deck of cards, i.e. 52"""
    deck = []
    for suit in ["♠", "♥", "♣", "♠"]:
        for i in range(2, 11):
            deck.append(f"{suit}{str(i)}")
        for i in ["A", "J", "Q", "K"]:
            deck.append(f"{suit}{i}")
    return deck

def shuffle_deck(deck):
    """ Shuffle the deck and return it """
    random.shuffle(deck)
    return deck

def draw_card(deck):
    """ Draw a card from input deck
    return card and the deck - that card """
    card = deck[-1]
    deck.pop()
    return (card, deck)

#d = create_deck()
#d = shuffle_deck(d)
#c, d = draw_card(d)
#print(c)
#print(len(d))

def calculate_points(hand):
    """ Calculate points of the given hand
    To-Do: At the moment it uses A as 11. Fix this to include 1 or 11.
    """
    points = 0
    for card in hand:
        if card[1:] in ["A"]:
            points += 11  # To-Do: Fix this logic later to include A=1
        elif card[1:] in ["J", "Q", "K"]:
            points += 10
        else:
            points += int(card[1:])
    return points

def check_blackjack(hand):
    """ Check if hand is A + J, K, Q """
    return True

def check_busted(hand):
    """ Check if a hand is > 21 """
    return True

#hand = ["♣5", "♣Q"]
#points = calculate_points(hand)
#print(points)
