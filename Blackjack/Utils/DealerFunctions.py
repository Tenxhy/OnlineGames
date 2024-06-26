from Cards import Deck
from Cards import Card
from Cards import Hand
from typing import List
import time

@staticmethod
class DealerFunctions:

    @staticmethod
    def getDealerCards(deck: Deck) -> Hand:
        card1, card2 = deck.drawCards(2)
        card2.setHiddenStatus(True)
        hand = Hand([card1, card2])
        return hand
    
    @staticmethod
    def hit(deck: Deck, hand: Hand) -> Hand:
        handCards = hand.getCards()
        handCards.append(deck.drawCard())
        hand.setCards(handCards)
        return hand
    
    @staticmethod
    def getHiddenCards(hand: Hand) -> Card | List[Card]:
        hiddenCards = []
        for card in hand.getCards():
            if card.getHiddenStatus():
                hiddenCards.append(card)
        
        if len(hiddenCards) == 1:
            return hiddenCards[0]
        else:
            return hiddenCards
    
    @staticmethod
    def revealHiddenCards(hand: Hand) -> Hand:
        for card in hand.getCards():
            if card.isHidden():
                card.setHiddenStatus(False)
                break
        return hand
    
    @staticmethod
    def printDealerHand(hand: list) -> None:
        print("# Dealer's hand: ", end="\n")
        for card in hand:
            if card.isHidden():
                card_display = """
\u250C\u2500\u2500\u2500\u2500\u2500\u2510
|     |
|     |
|     |
\u2514\u2500\u2500\u2500\u2500\u2500\u2518""".strip()
                print(card_display)
            else:
                card.display()
        print("#-----------------------------")
        time.sleep(2)