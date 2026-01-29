from Deck import Deck

class Solitaire:
    def __init__(self):
        self.deck = Deck()
        self.face_up = []

    def deal_until_four(self):
        while len(self.face_up) < 4 and self.deck.number_of_cards() > 0:
            self.face_up.append(self.deck.deal())

    def remove_four_same_suit(self) -> bool:
        if len(self.face_up) < 4:
            return False
        
        last_four = self.face_up[-4:]
        suit = last_four[0].get_suit()

        if all(card.get_suit() == suit for card in last_four):
            del self.face_up[-4:]
            return True
        
        return False
    
    