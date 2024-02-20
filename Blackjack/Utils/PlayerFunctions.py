from Cards import Deck
from Cards import Card
from Cards import Hand
from typing import List

@staticmethod
class PlayerFunctions:
    
    def getPlayerCards(deck: Deck) -> List[Card]:
        card1, card2 = deck.drawCards(2)
        hand = [card1, card2]
        return hand
    
    def hit(deck: Deck, hand: list) -> List[Card]:
        hand.append(deck.drawCard())
        return hand
    
    def doubleDown(deck: Deck, hand: List[Card]) -> List[Card]:
        hand = PlayerFunctions().hit(deck, hand)
        return hand
    
    def split(deck: Deck, hand: Hand) -> Hand:
        if len(hand.getCards()) == 2 and hand.getCards()[0].getValue() == hand.getCards()[1].getValue():
            newHandCards = []
            for i in range(2):
                newHandCards.append([hand[i], deck.drawCard()])
            hand.setCards(newHandCards)
            return hand
    