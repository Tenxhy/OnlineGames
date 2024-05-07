from .Suit import Suit
from .Value import Value
import os, yaml

display_ranks = []

with open(os.path.dirname(__file__) + r'\Displays.yml', 'r') as file:
    openedFile = yaml.safe_load(file)
    display_ranks = openedFile["cards"]["ranks"]

class Card():
    '''A class used to represent a game card'''
    def __init__(self, value: Value, suit: Suit, isHidden: bool = False):
        self.__value = value
        self.__suit = suit
        self.__isHidden = isHidden
    
    def getValue(self):
        return self.__value
    
    def getSuit(self):
        return self.__suit

    def getFormattedName(self):
        return str(self.getValue().name) + " OF " + str(self.getSuit().name)
    
    def isHidden(self):
        return self.__isHidden
    
    def setHiddenStatus(self, hidden_status: bool):
        self.__isHidden = hidden_status
    
    def get_display(self) -> list:
        value = str(self.getValue().value)
        if value == 10:
            if self.getValue().name.lower() in display_ranks.keys():
                value = display_ranks[self.getValue().name.lower()]

        [str(line).replace("X", value) for line in self.getSuit().get_display()]

    def display(self) -> None:
        [print(line) for line in self.get_display()]

    def __str__(self) -> str:
        return self.getFormattedName()
