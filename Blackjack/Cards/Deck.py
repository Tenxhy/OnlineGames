from .Card import Card
from .Value import Value
from .Suit import Suit
from typing import List
import random as rand

class Deck():
    '''A class used to represent a deck of cards'''
    def __init__(self, n_of_decks: int = 1) -> None:
        '''Creates a new Deck
        
        If no n_of_deck specified it defaults to 1

        Parameters
        ---
        n_of_decks : int, optional
            Number of 52 card decks to add to the new Deck
        
        Returns
        ---
        Deck
            The created Deck'''
        self._cards: List[Card] = []

        self.resetDeck(n_of_decks)
    
    def addCard(self, value: Value, suit: Suit) -> Card | None:
        '''Gets a list of N cards and removes them from the Deck
        
        If no n_of_cards specified it defaults to 1

        Parameters
        ---
        n_of_cards : int, optional
            Number of cards to draw
        '''
        if not (value in Value and suit in Suit):
            return None
        
        card = Card(value, suit)
        self._cards.append(card)

    def removeCard(self, value: Value, suit: Suit) -> Card:
        '''Removes the first card with the specified Value and Suit from the Deck

        Parameters
        ---
        value : Value
            Value of the card to remove
        
        suit : Suit
            Suit of the card to remove
            
        Raises
        ---
        ValueError
            If no card with the specified Value and Suit is found in the Deck
        
        Returns
        ---
        Card
            The removed card
        '''
        if not any((card.getValue() == value and card.getSuit() == suit) for card in self._cards):
            raise ValueError("Card not found in the deck")
        
        for eCard in self._cards:
            if eCard.getValue() == value and eCard.getSuit() == suit:
                self._cards.remove(eCard)
                return eCard
    
    def resetDeck(self, n_of_decks: int = 1) -> None:
        '''Resets the Deck
        
        If no n_of_decks specified it defaults to 1

        Parameters
        ---
        n_of_decks : int, optional
            Number of 52 card decks to add to the new Deck
        '''
        self._cards = []

        for i in range(n_of_decks):
            values = [value for value in Value]
            suits = [suit for suit in Suit]

            for value in values:
                for suit in suits:
                    self._cards.append(Card(value, suit))

    def getCards(self) -> List[Card]:
        '''Gets the list of cards contained in the Deck
        
        Returns
        ---
        List[Card]
            All the cards present in the Deck
        '''
        return self._cards
    
    def getCardsCount(self) -> int:
        '''Gets the number of cards contained in the Deck
        
        Returns
        ---
        int
            The number of cards in the Deck
        '''
        return len(self._cards)
    
    def drawCard(self) -> Card | None:
        '''Gets a card and removes it from the Deck
        
        Returns
        ---
        Card
            The drawn card
        
        None
            If no card was found in the deck
        '''
        if len(self._cards) <= 0:
            return None
        card = rand.choice(self._cards)
        result = self.removeCard(card.getValue(), card.getSuit())
        if result is None:
            return None
        return result
    
    def drawCards(self, n_of_cards: int = 1) -> List[Card] | None:
        '''Gets a list of N cards and removes them from the Deck
        
        If no n_of_cards specified it defaults to 1

        Parameters
        ---
        n_of_cards : int, optional
            Number of cards to draw
        
        Returns
        ---
        List[Card]
            The drawn cards
        '''
        cards = []
        for i in n_of_cards:
            card = self.drawCard()
            if not card is None:
                return None
            cards.append(card)
        
        return cards
    
    def __str__(self) -> str:
        strDeck = ""
        for card in self._cards:
            strDeck += str(card) + ", "
        return strDeck.strip()
    