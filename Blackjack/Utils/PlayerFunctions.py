from Cards import Deck
from Cards import Card
from Cards import Hand
from typing import List

@staticmethod
class PlayerFunctions:
    
    @staticmethod
    def getPlayerCards(deck: Deck) -> Hand:
        card1, card2 = deck.drawCards(2)
        hand = Hand([card1, card2])
        return hand
    
    @staticmethod
    def hit(deck: Deck, hand: Hand) -> Hand:
        handCards = hand.getCards()
        handCards.append(deck.drawCard())
        hand.setCards(handCards)
        return hand
    
    @staticmethod
    def doubleDown(deck: Deck, hand: Hand) -> List[Card]:
        hand = PlayerFunctions().hit(deck, hand)
        return hand
    
    @staticmethod
    def split(deck: Deck, hand: Hand) -> Hand:
        if len(hand.getCards()) == 2 and hand.getCards()[0].getValue() == hand.getCards()[1].getValue():
            newHandCards = []
            for i in range(2):
                newHandCards.append([hand.getCards()[i], deck.drawCard()])
            hand.split(newHandCards[0], newHandCards[1])
            return hand
    