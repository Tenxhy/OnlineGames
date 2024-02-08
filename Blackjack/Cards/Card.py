from .Suit import Suit
from .Value import Value

class Card():
    def __init__(self, value: Value, suit: Suit):
        self._value = value
        self._suit = suit
    
    def getValue(self):
        return self._value
    
    def getSuit(self):
        return self._suit

    def getFormattedName(self):
        return str(self.getValue().name) + " OF " + str(self.getSuit().name)
    