class Card:
    def __init__(self, suit: str, value: str):
        self._suit = suit
        self._value = value

    def get_suit(self) -> str:
        return self._suit
    
    def get_value(self) -> str:
        return self._value
    
    def __repr__(self) -> str:
        return f"{self._value} of {self._suit}"
    