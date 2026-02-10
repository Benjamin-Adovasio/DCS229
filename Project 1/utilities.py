"""
Reo
"""
from __future__ import annotations
from Card import Card

def sum_cards_iter(cards: list[Card]) -> int:
    total = 0
    for card in cards:
        total = total + card
    return total
#Added for project 2: Created a function to sum a list of Card objects using iteration.

def sum_cards_recursive(cards: list[Card]) -> int:
    if cards == []:
        return 0
    return cards[0] + sum_cards_recursive(cards[1:])
#Added for project 2: Created a function to sum a list of Card objects using recursion.

def test_sum_cards():
    cards = [
        Card("diamond", 5),
        Card("clubs", 3),
        Card("spade", 12),
        Card("clubs", 1)
    ]
    assert sum_cards_iter(cards) == 21
    assert sum_cards_recursive(cards) == 21
#Added for project 2: Example tests given