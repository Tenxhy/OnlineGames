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
    
    def getValue(self) -> Value:
        return self.__value
    
    def getValueInt(self) -> int:
        if self.__value.value > 10:
            return 10
        return self.__value.value
    
    def getSuit(self) -> Suit:
        return self.__suit

    def getFormattedName(self):
        return str(self.getValue().name) + " OF " + str(self.getSuit().name)
    
    def isHidden(self):
        return self.__isHidden
    
    def setHiddenStatus(self, hidden_status: bool):
        self.__isHidden = hidden_status
    
    def get_display(self) -> list:
        value = str(self.getValueInt())
        if int(value) >= 10:
            if self.getValue().name.lower() in display_ranks.keys():
                value = display_ranks[self.getValue().name.lower()]

        if (len(value) > 1):
            return [str(line).replace("XX", value) for line in self.getSuit().get_display()]
        else:
            n = 1
            displayed_card = self.getSuit().get_display()
            for i in range(len(displayed_card)):
                line = displayed_card[i]
                if "XX" not in line:
                    continue

                mValue = value
                if not (n % 2 == 0):
                    mValue += " "
                else:
                    mValue = " " + mValue
                line = str(line).replace("XX", mValue)
                displayed_card[i] = line
                n += 1
            
            return displayed_card

    def display(self) -> None:
        [print(line) for line in self.get_display()]

    def __str__(self) -> str:
        return self.getFormattedName()
