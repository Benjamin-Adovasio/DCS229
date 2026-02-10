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

    def __add__(self, other) -> int:
            #Adding 2 cards together
        if isinstance(other, Card):
            return self.value + other.value
        elif isinstance(other, int):
            #allows adding a card to an int
            return self.value + other
    #Added for project 2: Created an "__add__" meathod to allow adding Cards together.
