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

def calculate_totals(hand):
    """ Calculate points of the given hand
    Input: hand (array)
    Return: totals (array)
    """
    totals = []
    points_without_aces = 0
    aces_count = 0
    for card in hand:
        if card[1:] in ["A"]:
            aces_count += 1
        elif card[1:] in ["J", "Q", "K"]:
            points_without_aces += 10
        else:
            points_without_aces += int(card[1:])

    # Deal with As
    # total: total without Ace
    # if 1 A then:
    #  total_1 = total + 1
    #  total_2 = total + 11
    # if 2 As then:
    #  total_1 = total + 2
    #  total_2 = total + 12
    #  total_3 = total + 22
    # if 3 As then:
    #  total_1 = total + 3
    #  total_2 = total + 13
    #  total_3 = total + 23
    #  total_4 = total + 33
    # if 4 As then:
    #  total_1 = total + 4
    #  total_2 = total + 14
    #  total_3 = total + 24
    #  total_4 = total + 34
    #  total_5 = total + 44

    if aces_count == 0:
        totals.append(points_without_aces)
    elif aces_count == 1:
        totals.append(points_without_aces + 1)
        totals.append(points_without_aces + 11)
    elif aces_count == 2:
        totals.append(points_without_aces + 2)
        totals.append(points_without_aces + 12)
        totals.append(points_without_aces + 22)
    elif aces_count == 3:
        totals.append(points_without_aces + 3)
        totals.append(points_without_aces + 13)
        totals.append(points_without_aces + 23)
        totals.append(points_without_aces + 33)
    elif aces_count == 4:
        totals.append(points_without_aces + 4)
        totals.append(points_without_aces + 14)
        totals.append(points_without_aces + 24)
        totals.append(points_without_aces + 34)
        totals.append(points_without_aces + 44)
    return totals

def get_eligible_totals(totals):
    """ Return totals that are not busted """
    return [total for total in totals if total <= 21]

def check_blackjack(hand):
    """ Check if hand is A + J, K, Q """
    return True

def check_busted(hand):
    """ Check if a hand is > 21 """
    totals = calculate_totals(hand)
    busted_count = 0
    for total in totals:
        if total > 21:
            busted_count += 1
    return busted_count == len(totals)

def main():
    # Step 1: Initialize deck
    deck = create_deck()
    deck = shuffle_deck(deck)

    # Step 2: Initialize hands
    player_hand = []
    computer_hand = []

    for i in range(2):
        card, deck = draw_card(deck)
        player_hand.append(card)

    for i in range(2):
        card, deck = draw_card(deck)
        computer_hand.append(card)

    print(f"Player's Hand: {player_hand}. Totals: {calculate_totals(player_hand)}")
    print(f"Computer's Hand: {computer_hand[0]}, ??")

    # Step 3: Let the user play
    user_turn = True
    while user_turn:
        # Handle user choices
        decision = input("Your turn. (H)it or (S)tand?")
        if decision == "h":
            card, deck = draw_card(deck)
            player_hand.append(card)
            print(f"Player's Hand: {player_hand}. Totals: {calculate_totals(player_hand)}")
        elif decision == "s":
            user_turn = False
            print("Player stands. It's now Computer's turn.")
        else:
            print("Invalid choice. Select (h) or (s).")

        # Check if the game is over
        if check_busted(player_hand):
            user_turn = False
            print("Player has busted. You lose the game!")
    print(f"Hello {decision}")

    # Step 4: Make the computer play
 
    # if max eligible totals < 17 then:
    #   computer draws
    # if 17 =< max eligible totals =< 21 then:
    #   computer stands
    # if all totals > 21 then:
    #   computer loses the game

    computer_active = True
    while computer_active:
        print(f"Computer's Hand: {computer_hand}")
        computer_totals = calculate_totals(computer_hand)
        computer_eligible_totals = get_eligible_totals(computer_totals)
        if len(computer_eligible_totals) == 0:
            computer_active = False
            print("Computer has busted. You win the game!")
        elif max(computer_eligible_totals) >= 17:
            computer_active = False
            print(f"Computer stands with {max(computer_eligible_totals)}.")
        else:
            card, deck = draw_card(deck)
            computer_hand.append(card)
            print(f"Computer draws {card}")

    # Step 5: Find out who wins
    

main()
