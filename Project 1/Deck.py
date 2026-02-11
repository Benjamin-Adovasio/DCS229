import random
from Card import Card

"""
Defines the deck of cards used in the Solitaire game. Contains methods to shuffle the deck, deal cards, and check the number of remaining cards.

Important Note: The prints in this file only run when this file is ececuted directly. This file should not be executed directly normally.
"""
class Deck:
    def __init__(self):
        self._cards= []
        self._next_card = 0

        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] #the possible suits
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] #the possible values

        for suit in suits:
            for value in values:
                self._cards.append(Card(suit, value)) #creates a standard 52-card deck
    
    def shuffle(self):
        for i in range(len(self._cards)): #iterates through each card in the deck
            j = random.randrange(i, len(self._cards)) #selects a random index from i to the end of the deck
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i] #Shuffles the deck
        self._next_card = 0    #Resets the next card index after shuffling.
    
    def deal(self):
        if self._next_card >= len(self._cards): 
            return None #Returns None if there are no cards left to deal.
        card = self._cards[self._next_card]
        self._next_card += 1 #Advances the next card index.
        return card
    
    def number_of_cards(self) -> int:
        return len(self._cards) - self._next_card #Returns the number of remaining cards in the deck.
    
if __name__ == "__main__":
    deck = Deck()
    deck.shuffle() #Calls the shuffle method to randomize the deck.
    for _ in range(5):
        print(deck.deal())
    print("Cards left:", deck.number_of_cards()) #Prints the number of cards left in the deck after dealing five cards. 