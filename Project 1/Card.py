######################################
# DCS 229 -- Unfair Solitaire 
# This is the Card.py file, which defines the Card class used in the Solitaire game. The Card class represents a playing card with a suit and value, and includes methods to retrieve the suit and value, as well as a string representation of the card.
# Date: 04/01/2026
# Name: Benjamin Adovasio
# Resources Used: Fran 
##########################################
class Card:
    """
    Represents a playing card with a suit and value.
    """
    def __init__(self, suit: str, value: str):
        self._suit = suit
        self._value = value
    #Creates a Card object with the specified suit and value.

    def get_suit(self) -> str:
        return self._suit
    
    #Returns the suit of the card.
    
    def get_value(self) -> str:
        return self._value
    #Returns the value of the card.
    
    def __repr__(self) -> str:
        return f"{self._value} of {self._suit}"
    
    #Returns a string representation of the card in the format "Value of Suit".

if __name__ == "__main__":
    card1 = Card("Hearts", "Ace")
    card2 = Card("Spades", "10")

    assert card1.get_suit() == "Hearts"
    assert card1.get_value() == "Ace"
    assert card2.get_suit() == "Spades"
    assert card2.get_value() == "10"

    assert repr(card1) == "Ace of Hearts"
    assert repr(card2) == "10 of Spades"

    print("All Card tests passed.")