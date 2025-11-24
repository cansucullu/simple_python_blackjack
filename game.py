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
