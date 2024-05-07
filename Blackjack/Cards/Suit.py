from enum import Enum, auto
import os, yaml

display_card = []
display_symbols = []

with open(os.path.dirname(__file__) + r'\Displays.yml', 'r') as file:
    openedFile = yaml.safe_load(file)
    display_card = openedFile["cards"]["display"]
    display_symbols = openedFile["cards"]["symbols"]

class Suit(Enum):

    SPADES = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    HEARTS = auto()

    def get_display(self) -> list:
        symbol = "Y"
        if self == Suit.SPADES:
            symbol = display_symbols[self.name.lower()]
        elif self == Suit.DIAMONDS:
            symbol = display_symbols[self.name.lower()]
        elif self == Suit.CLUBS:
            symbol = display_symbols[self.name.lower()]
        elif self == Suit.HEARTS:
            symbol = display_symbols[self.name.lower()]
        
        displayCard = [str(line).replace("Y", symbol) for line in display_card]
        return displayCard

print(Suit.SPADES.get_display())

