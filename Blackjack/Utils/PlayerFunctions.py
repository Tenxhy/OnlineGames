from Cards import Deck
from Cards import Card
from Cards import Hand
from typing import List
import time

@staticmethod
class PlayerFunctions:
    
    @staticmethod
    def getPlayerCards(deck: Deck) -> Hand:
        card1, card2 = deck.drawCards(2)
        hand = Hand([card1, card2])
        return hand

    '''Hit function for the player
    
    If the player has split, then the card is added to the first hand
    If the player has split and the hand number is 1, then the card is added to the second hand

    Parameters
    ---
    deck : Deck
        The deck to draw the card from
    hand : Hand
        The hand to add the card to
    hand_number : int, optional
        Hand number to hit if the player has split, defaults to 1
    
    Returns
    ---
    Hand
        The hit hand'''
    @staticmethod
    def hit(deck: Deck, hand: Hand, hand_number: int = 1) -> Hand:
        if not hand.isSplit():
            handCards = hand.getCards()
            handCards.append(deck.drawCard())
            hand.setCards(handCards)
        else:
            handCards = hand.getCards()
            handCards[hand_number-1].append(deck.drawCard())
            hand.setCards(handCards)
        return hand
    
    @staticmethod
    def doubleDown(deck: Deck, hand: Hand) -> Hand:
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
        
    def printPlayerHands(dealerHand: List[Card], playerHand: List[Card]):

        if type(playerHand[0]) != type([]):
            print("# Your hand: ", end="\n")
            for card in playerHand:
                card.display()
            print("#")
            time.sleep(2)
        else:
            for i in range(len(playerHand)):
                hand = playerHand[i]
                print(f"# Your {i+1}° hand: ", end="\n")
                for card in hand:
                    card.display()
                print("#")
                time.sleep(1)
    