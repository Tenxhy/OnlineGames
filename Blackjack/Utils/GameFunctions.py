from Cards import Deck
from Cards import Card
from Cards import Value
from Cards import Suit
from Utils import DealerFunctions
from Utils import PlayerFunctions

from typing import List

@staticmethod
class GameFunctions:
    def getDealedCards(deck: Deck) -> List[List[Card], List[Card]]:
        dealerHand = DealerFunctions().getDealerCards(deck)
        playerHand = PlayerFunctions().getPlayerCards(deck)
        return dealerHand, playerHand
    
    def getHandValue(hand: List[Card]) -> int:
        value = 0
        for card in hand:
            if card.getValue() == Value.ACE:
                if value + 11 > 21:
                    value += 1
                else:
                    value += 11
            else:
                value += card.getValue().value
        return value
    
    def isBlackjack(hand: List[Card]) -> bool:
        return len(hand) == 2 and GameFunctions().getHandValue(hand) == 21
    
    def isBust(hand: List[Card]) -> bool:
        return GameFunctions().getHandValue(hand) > 21
    
    def checkWinner(dealerHand: List[Card], playerHand: List[Card]):
        if GameFunctions().isBust(dealerHand):
            return "Player wins"
        elif GameFunctions().isBust(playerHand):
            return "Dealer wins"
        elif GameFunctions().getHandValue(dealerHand) > GameFunctions().getHandValue(playerHand):
            return "Dealer wins"
        elif GameFunctions().getHandValue(dealerHand) < GameFunctions().getHandValue(playerHand):
            return "Player wins"
        else:
            return "Push" 
        
    
    def playAgain():
        pass
