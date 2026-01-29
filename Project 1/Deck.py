import random
from Card import Card

class Deck:
    def __init__(self):
        self._cards= []
        self._next_card = 0

        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] #the possible suits
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] #the possible values

        for suit in suits:
            for value in values:
                self._cards.append(Card(suit, value))
    