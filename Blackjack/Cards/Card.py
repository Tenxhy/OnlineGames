from .Suit import Suit
from .Value import Value

class Card():
    '''A class used to represent a game card'''
    def __init__(self, value: Value, suit: Suit):
        self._value = value
        self._suit = suit
    
    def getValue(self):
        return self._value
    
    def getSuit(self):
        return self._suit

    def getFormattedName(self):
        return str(self.getValue().name) + " OF " + str(self.getSuit().name)
    
    def __str__(self) -> str:
        return self.getFormattedName()
    