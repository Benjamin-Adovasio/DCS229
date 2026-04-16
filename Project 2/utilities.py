######################################
# DCS 229 -- Project 2
# This is the utilities.py file, which contains utility functions for the Solitaire game.
# Date: 04/01/2026
# Name: Benjamin Adovasio
# Resources Used: Fran 
##########################################

from __future__ import annotations
from Card import Card

'''
Added for project 2: Created a function to sum a list of Card objects using iteration.
'''
def sum_cards_iter(cards: list[Card]) -> int: #start total at 0
    total = 0 #start total at 0
    for card in cards:
        total = total + card #Adds the value of each card to the total using iteration.
    return total

'''
Added for project 2: Created a function to sum a list of Card objects using recursion.
'''
def sum_cards_recursive(cards: list[Card]) -> int: #start total at 0
    if cards == []:
        #Base case
        return 0 #If the list of cards is empty, return 0.
    return cards[0] + sum_cards_recursive(cards[1:]) #Adds the value of the first card to the sum of the remaining cards using recursion.
    #Recursive case


'''
Added for project 2: Example tests given
'''
def test_sum_cards():
    cards = [
        Card("diamond", 5),
        Card("clubs", 3),
        Card("spade", 12),
        Card("clubs", 1)
    ]
    print(sum_cards_iter(cards))
    # assert sum_cards_iter(cards) == 21
    # assert sum_cards_recursive(cards) == 21

test_sum_cards()