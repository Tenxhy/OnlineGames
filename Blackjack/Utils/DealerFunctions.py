from Cards import Deck
from Cards import Card
from Cards import Hand
from typing import List

@staticmethod
class DealerFunctions:

    @staticmethod
    def getDealerCards(deck: Deck) -> Hand:
        card1, card2 = deck.drawCards(2)
        hand = Hand([card1, card2])
        return hand
    
    @staticmethod
    def hit(deck: Deck, hand: Hand) -> Hand:
        handCards = hand.getCards()
        handCards.append(deck.drawCard())
        hand.setCards(handCards)
        return hand
    