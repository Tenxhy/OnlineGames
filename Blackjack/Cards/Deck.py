from .Card import Card
from .Value import Value
from .Suit import Suit
import random as rand

class Deck():
    def __init__(self, n_of_decks: int = 1) -> None:
        self._cards = []

        self.resetDeck(n_of_decks)
    
    def addCard(self, value: Value, suit: Suit) -> Card | None:
        if not (value in Value and suit in Suit):
            return None
        
        card = Card(value, suit)
        self._cards.append(card)

    def removeCard(self, value: Value, suit: Suit) -> Card | None:
        if not any((card.getValue() == value and card.getSuit() == suit) for card in self._cards):
            raise Exception("Card not found in the deck")
        
        for eCard in self._cards:
            if eCard.getValue() == value and eCard.getSuit() == suit:
                self._cards.remove(eCard)
                return eCard
    
    def resetDeck(self, n_of_decks: int = 1) -> None:
        self._cards = []

        for i in range(n_of_decks):
            values = [value for value in Value]
            suits = [suit for suit in Suit]

            for value in values:
                for suit in suits:
                    self._cards.append(Card(value, suit))

    def getCards(self) -> list:
        return self._cards
    
    def getCardsCount(self) -> int:
        return len(self._cards)
    
    def drawCard(self) -> Card | None:
        card = rand.choice(self._cards)
        result = self.removeCard(card.getValue(), card.getSuit())
        if result == None:
            return None
        return result
    