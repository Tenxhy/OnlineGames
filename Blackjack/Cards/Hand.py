from .Card import Card
from typing import List

class Hand:
    def __init__(self, cards: List[Card]) -> None:
        self._cards = []
        self._split = False

    def isSplit(self) -> bool:
        return self._split
    
    def getCards(self):
        return self._cards
    
    def setCards(self, cards: List[Card]):
        self._cards = cards
    
    def split(self, hand1: List[Card], hand2: List[Card]) -> None:
        self._split = True
        self._cards = [hand1, hand2]
        return self._cards
    