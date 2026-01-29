from Deck import Deck
"""
Defines the Solitaire game logic. Contains methods to play the game by dealing cards, removing cards based on game rules, and checking for a win condition.

Important Note: The prints in this file only run when this file is ececuted directly. This file should not be executed directly normally.
"""

class Solitaire:
    def __init__(self):
        self.deck = Deck()
        self.face_up = [] #List to hold face-up cards.

    def deal_until_four(self):
        while len(self.face_up) < 4 and self.deck.number_of_cards() > 0:
            self.face_up.append(self.deck.deal()) #Deals cards until there are four face-up cards.

    def remove_four_same_suit(self) -> bool:
        if len(self.face_up) < 4:
            return False #Not enough cards to remove four of the same suit.
        
        last_four = self.face_up[-4:]
        suit = last_four[0].get_suit()

        if all(card.get_suit() == suit for card in last_four):
            del self.face_up[-4:]
            return True #Removed four cards of the same suit.
        
        return False
    
    def remove_inner_two(self) -> bool:
        if len(self.face_up) < 4:
            return False #Not enough cards to remove inner two cards.

        last_four = self.face_up[-4:]
        if last_four[0].get_suit() == last_four[3].get_suit():
            del self.face_up[-3:-1]
            return True #Removed inner two cards.

        return False

    def remove_all_possible(self):
        removed = True
        while removed and len(self.face_up) >= 4:
            removed = self.remove_four_same_suit()
            if not removed:
                removed = self.remove_inner_two() # Attempts to remove cards based on game rules.

    def playGame(self) -> bool:
        self.deck.shuffle()
        self.face_up = []

        self.deal_until_four() #Deals cards until there are four face-up cards.

        while self.deck.number_of_cards() > 0:
            self.remove_all_possible()
            self.face_up.append(self.deck.deal())

        self.remove_all_possible()
        return len(self.face_up) == 0  #   Checks for a win condition.
    
if __name__ == "__main__":
    game = Solitaire()
    print("win?", game.playGame()) #Prints whether the game was won or not. Not normally executed.