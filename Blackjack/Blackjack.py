import yaml
import random as rand
from colorama import Fore, Back, Style
from Cards import Deck
from Cards import Value
from Utils import DealerFunctions
from Utils import PlayerFunctions
from Utils import GameFunctions
from Cards import Hand

deck = Deck(4)

class Blackjack():

    def play(self):

        print("""
#################################################################
#\t\t            BLACKJACK           \t\t#
#################################################################""".strip())
        print("#")

        balance = float(input("# Enter your balance: "))

        while balance > 0:
            bet = GameFunctions().placeBet()
            dealerHand, playerHand = GameFunctions().getDealedCards(deck)
            playerHand.setCards([playerHand.getCards()[0], playerHand.getCards()[0]]) # DEBUG

            GameFunctions().printInitialHands(dealerHand.getCards(), playerHand.getCards())

            if GameFunctions().isBlackjack(playerHand):
                print("Blackjack! You win!")
                balance += bet*1.5

            else:
                while not GameFunctions().isBust(playerHand):
                    choice = input("What do you want to do with your first hand? 'hit' | 'stand' | 'double' | 'split'  ")

                    if choice == "hit":
                        playerHand = PlayerFunctions().hit(deck, playerHand)
                        GameFunctions().printHands(dealerHand.getCards(), playerHand.getCards())

                    elif choice == "double":
                        if balance < bet*2:
                            print("You don't have enough money to double down.")
                        else:
                            bet *= 2
                            playerHand = PlayerFunctions().doubleDown(deck, playerHand)
                            GameFunctions().printHands(dealerHand.getCards(), playerHand.getCards())
                            break

                    elif choice == "split":
                        if playerHand.getCards()[0].getValue() != playerHand.getCards()[1].getValue() or balance < bet*2:
                            print("You can only split if you have two cards of the same value and if you have enough money.")
                        else:
                            playerHand = PlayerFunctions().split(deck, playerHand)
                            GameFunctions().printInitialHands(dealerHand.getCards(), playerHand.getCards())

                            while not GameFunctions().isBust(Hand(playerHand.getCards()[0])):
                                choice1 = input("What do you want to do? 'hit' | 'stand' | 'double' ")

                                if choice1 == "hit":
                                    playerHand = PlayerFunctions().hit(deck, playerHand, 1)
                                    GameFunctions().printSplitHands(playerHand.getCards(), 1)
                                elif choice1 == "double":
                                    if balance < bet*2:
                                        print("You don't have enough money to double down.")
                                    else:
                                        bet *= 2
                                        playerHand = PlayerFunctions().doubleDown(deck, playerHand)
                                        GameFunctions().printSplitHands(playerHand.getCards(), 1)
                                        break
                                else:
                                    break

                            if GameFunctions().isBust(Hand(playerHand.getCards()[0])):
                                print("Bust! Dealer wins!")
                                balance -= bet

                            toBreak = True
                            
                            while not GameFunctions().isBust(Hand(playerHand.getCards()[1])):
                                choice2 = input("What do you want to do with your second hand? 'hit' | 'stand' | 'double' ")

                                if choice2 == "hit":
                                    playerHand = PlayerFunctions().hit(deck, playerHand, 2)
                                    GameFunctions().printSplitHands(playerHand.getCards(), 2)
                                
                                elif choice2 == "double":
                                    if balance < bet*2:
                                        print("You don't have enough money to double down.")
                                    else:
                                        bet *= 2
                                        playerHand = PlayerFunctions().doubleDown(deck, playerHand)
                                        GameFunctions().printSplitHands(playerHand.getCards(), 2)
                                        break
                                else:
                                    break

                            if GameFunctions().isBust(Hand(playerHand.getCards()[1])):
                                print("Bust! Dealer wins!")
                                balance -= bet
                            
                            toBreak = True
                    else:
                        break

                    if toBreak:
                        break
                
                if not playerHand.isSplit():
                    if GameFunctions().isBust(playerHand):
                        print("Bust! Dealer wins!")
                        balance -= bet

                    else:
                        while GameFunctions().getHandValue(dealerHand) < 17:
                            dealerHand = DealerFunctions().hit(deck, dealerHand)
                            GameFunctions().printHands(dealerHand.getCards(), playerHand.getCards())

                        if GameFunctions().isBust(dealerHand):
                            print("Dealer busts! You win!")
                            balance += bet

                        else:
                            print(GameFunctions().checkWinner(dealerHand, playerHand))

                            if GameFunctions().checkWinner(dealerHand, playerHand) == "Player wins":
                                balance += bet

                            elif GameFunctions().checkWinner(dealerHand, playerHand) == "Dealer wins":
                                balance -= bet

                            else:
                                pass
                else:
                    for hand in playerHand.getCards():
                        hand = Hand(hand)
                        if GameFunctions().isBust(hand):
                            print("Bust! Dealer wins!")
                            balance -= bet
                            hand.getCards().remove(hand)
                        
                        else:
                            while GameFunctions().getHandValue(dealerHand) < 17:
                                dealerHand = DealerFunctions().hit(deck, dealerHand)
                                GameFunctions().printHands(dealerHand.getCards(), hand.getCards()) # FIXME: stop printing it twice

                            if GameFunctions().isBust(dealerHand):
                                print("Dealer busts! You win!")
                                balance += bet

                            else:
                                print(GameFunctions().checkWinner(dealerHand, hand))

                                if GameFunctions().checkWinner(dealerHand, hand) == "Player wins":
                                    balance += bet

                                elif GameFunctions().checkWinner(dealerHand, hand) == "Dealer wins":
                                    balance -= bet

                                else:
                                    pass

            print(f"Your balance: {balance}")

            if balance > 0:
                playAgain = input("Do you want to play again? ")
                if playAgain == "no":
                    break

            else:
                print("You have no more money to play.")
                break

        print("Thanks for playing!")