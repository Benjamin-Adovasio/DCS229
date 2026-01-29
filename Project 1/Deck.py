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
    
    def shuffle(self):
        for i in range(len(self._cards)):
            j = random.randomrange(i, len(self._cards))
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i]
        self._next_card = 0    
    
    def deal(self):
        if self._next_card >= len(self._cards):
            return None
        card = self._cards[self._next_card]
        self._next_card += 1
        return card
    
    def number_of_cards(self) -> int:
        return len(self._cards) - self._next_card
    
    if __name__ == "__main__":
        deck = Deck()
        print("Initial deck:")
        for card in deck._cards:
            print(card)
        
        deck.shuffle()
        print("\nShuffled deck:")
        for card in deck._cards:
            print(card)
        
        print("\nDealing cards:")
        while True:
            card = deck.deal()
            if card is None:
                break
            print(card)
        
        print(f"\nNumber of cards left in deck: {deck.number_of_cards()}")