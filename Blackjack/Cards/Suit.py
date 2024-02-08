from enum import Enum, auto

class Suit(Enum):

    SPADES = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    HEARTS = auto()

Suit = Enum('Suit', ['SPADES', 'DIAMONDS', 'CLUBS', 'HEARTS'])