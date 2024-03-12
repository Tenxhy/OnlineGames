from Cards import Deck
from Cards import Card
from Cards import Value
from Cards import Suit
from Utils import DealerFunctions
from Utils import PlayerFunctions
from Cards import Hand

import time
from typing import List, Union
from deprecated import deprecated

@staticmethod
class GameFunctions:

    @staticmethod
    def placeBet() -> float:
        bet = float(input("Enter your bet: "))
        return bet

    @staticmethod
    def getDealedCards(deck: Deck) -> List[Hand]:
        dealerHand = DealerFunctions().getDealerCards(deck)
        playerHand = PlayerFunctions().getPlayerCards(deck)
        return dealerHand, playerHand
    
    @staticmethod
    def getHandValue(hand: List[Card]) -> int:
        value = 0
        if type(hand) == type(Hand()):
            hand = hand.getCards()

        for card in hand:
            if card.getValue() == Value.ACE:
                if value + 11 > 21:
                    value += 1
                else:
                    value += 11
            else:
                value += card.getValue().value
            
            if value > 21:
                for card in hand:
                    if card.getValue() == Value.ACE:
                        value -= 10
                        if value <= 21:
                            break
        return value

    @staticmethod
    def printHands(dealerHand: List[Card], playerHand: List[Card]):

        if type(playerHand[0]) != type([]):
            DealerFunctions().printDealerHand(dealerHand)
            print("Your hand: ", end="")
            for card in playerHand:
                print(str(card), end=" | ")
            print("")
        else:
            DealerFunctions().printDealerHand(dealerHand)
            for i in range(len(playerHand)):
                hand = playerHand[i]
                print(f"Your {i+1}° hand: ", end="")
                for card in hand:
                    print(str(card), end=" | ")
                print("")

    @staticmethod
    def printSplitHands(playerHand: List[Card], n_of_hand: int = None):
        if n_of_hand != None:
            hand = playerHand[n_of_hand-1]
            print(f"Your {n_of_hand}° hand: ", end="")
            for card in hand:
                print(str(card), end=" | ")
            print("")
        else:
            for i in range(len(playerHand)):
                hand = playerHand[i]
                print(f"Your {i+1}° hand: ", end="")
                for card in hand:
                    print(str(card), end=" | ")
                print("")
                time.sleep(2)
    
    @staticmethod
    def isBlackjack(hand: Hand) -> bool:
        hand = hand.getCards()
        return len(hand) == 2 and type(hand[0]) != type([]) and GameFunctions().getHandValue(hand) == 21
    
    @staticmethod
    def isBust(hand: Hand) -> bool:
        return GameFunctions().getHandValue(hand.getCards()) > 21
    
    @staticmethod
    def checkWinner(dealerHand: Hand, playerHand: Hand, balance: float, bet: float) -> Union[str, float] | Union[List[str], float]:
        result = ""
        if not playerHand.isSplit():
            if GameFunctions().isBust(dealerHand):
                result = "Player wins"
            elif GameFunctions().isBust(playerHand):
                result = "Dealer wins"
            elif GameFunctions().getHandValue(dealerHand.getCards()) > GameFunctions().getHandValue(playerHand.getCards()):
                result = "Dealer wins"
            elif GameFunctions().getHandValue(dealerHand.getCards()) < GameFunctions().getHandValue(playerHand.getCards()):
                result = "Player wins"
            else:
                result = "Push"
        else:
            for i in range(len(playerHand.getCards())):
                hand = Hand(playerHand.getCards()[i])
                if GameFunctions().isBust(dealerHand):
                    result.append("Player wins round " + str(i+1))
                elif GameFunctions().isBust(hand):
                    result.append("Dealer wins " + str(i+1))
                elif GameFunctions().getHandValue(dealerHand.getCards()) > GameFunctions().getHandValue(hand.getCards()):
                    result.append("Dealer wins " + str(i+1))
                elif GameFunctions().getHandValue(dealerHand.getCards()) < GameFunctions().getHandValue(hand.getCards()):
                    result.append("Player wins " + str(i+1))
                else:
                    result.append("Push")
                
        balance = GameFunctions().balanceRefresh(balance, bet, result)
        return result, balance
    
    @staticmethod
    def balanceRefresh(balance: float, bet: float, result: str) -> float:
        if result.startswith("Player wins"):
            balance += bet
        elif result.startswith("Dealer wins"):
            balance -= bet
        return balance
