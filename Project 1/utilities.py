from __future__ import annotations
from Card import Card

def sum_cards_iter(cards: list[Card]) -> int:
    total = 0
    for card in cards:
        total = total + card
    return total
#Added for project 2: Created a function to sum a list of Card objects using iteration.

