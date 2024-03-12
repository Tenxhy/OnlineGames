from .Suit import Suit
from .Value import Value

class Card():
    '''A class used to represent a game card'''
    def __init__(self, value: Value, suit: Suit, isHidden: bool = False):
        self._value = value
        self._suit = suit
        self._isHidden = isHidden
    
    def getValue(self):
        return self._value
    
    def getSuit(self):
        return self._suit

    def getFormattedName(self):
        return str(self.getValue().name) + " OF " + str(self.getSuit().name)
    
    def isHidden(self):
        return self._isHidden
    
    def setHiddenStatus(self, hidden_status: bool):
        self._isHidden = hidden_status
    
    def __str__(self) -> str:
        return self.getFormattedName()
    