from Cards import Deck
from Cards import Card
from Cards import Value
from Cards import Suit
from Utils import DealerFunctions
from Utils import PlayerFunctions
from Cards import Hand

from typing import List

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
        return value
    
    @staticmethod
    def printInitialHands(dealerHand: List[Card], playerHand: List[Card]):
        print("Dealer's hand: ", end="")
        print(str(dealerHand[0]), end=" ")
        print("")
        print("Your hand: ", end="")
        print(str(playerHand[0]), end=" | ")
        print(str(playerHand[1]))

    @staticmethod
    def printHands(dealerHand: List[Card], playerHand: List[Card]):
        print("Dealer's hand: ", end="")
        for card in dealerHand:
            print(str(card), end=" | ")
        print("")

        if type(playerHand[0]) != type([]):
            print("Your hand: ", end="")
            for card in playerHand:
                print(str(card), end=" | ")
            print("")
        else:
            for i in range(len(playerHand)):
                hand = playerHand[i]
                print(f"Your {i+1}° hand: ", end="")
                for card in hand:
                    print(str(card), end=" | ")
                print("")
    
    @staticmethod
    def isBlackjack(hand: Hand) -> bool:
        hand = hand.getCards()
        return len(hand) == 2 and type(hand[0]) != type([]) and GameFunctions().getHandValue(hand) == 21
    
    @staticmethod
    def isBust(hand: Hand) -> bool:
        hand = hand.getCards()
        return GameFunctions().getHandValue(hand) > 21
    
    @staticmethod
    def checkWinner(dealerHand: Hand, playerHand: Hand) -> str:
        if playerHand.isSplit():
            if GameFunctions().isBust(dealerHand):
                return "Player wins"
            elif GameFunctions().isBust(playerHand):
                return "Dealer wins"
            elif GameFunctions().getHandValue(dealerHand.getCards()) > GameFunctions().getHandValue(playerHand.getCards()):
                return "Dealer wins"
            elif GameFunctions().getHandValue(dealerHand.getCards()) < GameFunctions().getHandValue(playerHand.getCards()):
                return "Player wins"
            else:
                return "Push"
        else:
            for i in range(len(playerHand.getCards())):
                hand = Hand(playerHand.getCards()[i])
                if GameFunctions().isBust(dealerHand):
                    return "Player wins round " + str(i+1)
                elif GameFunctions().isBust(hand):
                    return "Dealer wins " + str(i+1)
                elif GameFunctions().getHandValue(dealerHand.getCards()) > GameFunctions().getHandValue(hand.getCards()):
                    return "Dealer wins " + str(i+1)
                elif GameFunctions().getHandValue(dealerHand.getCards()) < GameFunctions().getHandValue(hand.getCards()):
                    return "Player wins " + str(i+1)
                else:
                    return "Push"
    
    @staticmethod
    def balanceRefresh(balance: float, bet: float, result: str) -> float:
        if result == "Player wins":
            balance += bet
        elif result == "Dealer wins":
            balance -= bet
        return balance
