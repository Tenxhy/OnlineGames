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
            

            GameFunctions().printHands(dealerHand.getCards(), playerHand.getCards())
            
            if GameFunctions().isBlackjack(playerHand):
                print("Blackjack! You win!")
                balance += bet*1.5

            # TODO: If the dealer has an ace, the player can take insurance
                
            else:
                toBreak = False
                while not GameFunctions().isBust(playerHand):
                    print("")

                    if GameFunctions().getHandValue(playerHand) == 21:
                        break

                    if len(playerHand.getCards()) == 2:
                        choice = input("What do you want to do? 'hit' | 'stand' | 'double' | 'split' ")
                    else:
                        choice = input("What do you want to do? 'hit' | 'stand' | 'split' ")
                    
                    match choice:

                        case "hit":
                            playerHand = PlayerFunctions().hit(deck, playerHand)
                            GameFunctions().printHands(dealerHand.getCards(), playerHand.getCards())

                        case "double":
                            if type(playerHand[0]) != type([]):
                                
                                if balance < (bet*2)+bet:
                                    print("You don't have enough money to double down.")
                                else:
                                    bet *= 2
                                    playerHand = PlayerFunctions().doubleDown(deck, playerHand)
                                    GameFunctions().printHands(dealerHand.getCards(), playerHand.getCards())
                                    break
                                
                            else:
                                if balance < (bet*2)+bet:
                                    print("You don't have enough money to double down.")
                                else:
                                    bet *= 2
                                    playerHand = PlayerFunctions().doubleDown(deck, playerHand)
                                    GameFunctions().printHands(dealerHand.getCards(), playerHand.getCards())
                                    break

                        case "split":
                            if playerHand.getCards()[0].getValue() != playerHand.getCards()[1].getValue() or balance < bet*2:
                                print("You can only split if you have two cards of the same value and if you have enough money.")
                            else:
                                playerHand = PlayerFunctions().split(deck, playerHand)
                                GameFunctions().printHands(dealerHand.getCards(), playerHand.getCards())

                                while not GameFunctions().isBust(Hand(playerHand.getCards()[0])):
                                    print("")
                                    if GameFunctions().getHandValue(Hand(playerHand.getCards()[0])) == 21:
                                        break

                                    if len(playerHand.getCards()[1]) == 2:
                                        choice1 = input("What do you want to do with your first hand? 'hit' | 'stand' | 'double' ")
                                    else:
                                        choice1 = input("What do you want to do with your first hand? 'hit' | 'stand' ")

                                    match choice1:

                                        case "hit":
                                            playerHand = PlayerFunctions().hit(deck, playerHand, 1)
                                            GameFunctions().printSplitHands(playerHand.getCards(), 1)
                                        case "double":
                                            if balance < bet*2:
                                                print("You don't have enough money to double down.")
                                            else:
                                                bet *= 2
                                                playerHand = PlayerFunctions().doubleDown(deck, playerHand)
                                                GameFunctions().printSplitHands(playerHand.getCards(), 1)
                                                break
                                        case "stand":
                                            break

                                        case _:
                                            print("Invalid choice. Try again.")

                                if GameFunctions().isBust(Hand(playerHand.getCards()[0])):
                                    print("Bust! Dealer wins!")
                                    balance -= bet

                                toBreak = True
                                
                                while not GameFunctions().isBust(Hand(playerHand.getCards()[1])):
                                    print("")
                                    if GameFunctions().getHandValue(Hand(playerHand.getCards()[0])) == 21:
                                        break
                                    
                                    if len(playerHand.getCards()[1]) == 2:
                                        choice2 = input("What do you want to do with your second hand? 'hit' | 'stand' | 'double' ")
                                    else:
                                        choice2 = input("What do you want to do with your second hand? 'hit' | 'stand' ")

                                    match choice2:
                                        
                                        case "hit":
                                            playerHand = PlayerFunctions().hit(deck, playerHand, 2)
                                            GameFunctions().printSplitHands(playerHand.getCards(), 2)
                                        
                                        case "double":
                                            if len(playerHand.getCards()[1]) == 2:
                                                print("Invalid choice. Try again.")

                                            else:
                                                if balance < bet*2:
                                                    print("You don't have enough money to double down.")
                                                else:
                                                    bet *= 2
                                                    playerHand = PlayerFunctions().doubleDown(deck, playerHand)
                                                    GameFunctions().printSplitHands(playerHand.getCards(), 2)
                                                    break
                                        case "stand":
                                            break

                                        case _:
                                            print("Invalid choice. Try again.")

                                if GameFunctions().isBust(Hand(playerHand.getCards()[1])):
                                    print("Bust! Dealer wins!")
                                    balance -= bet
                                
                                toBreak = True
                        case "stand":

                            break

                        case _:
                            print("Invalid choice. Try again.")

                    if toBreak:
                        break

                DealerFunctions().revealHiddenCards(dealerHand)
                DealerFunctions().printDealerHand(dealerHand.getCards())

                if not playerHand.isSplit():
                    if GameFunctions().isBust(playerHand):
                        print("Bust! Dealer wins!")
                        balance -= bet

                    else:
                        while GameFunctions().getHandValue(dealerHand) < 17:
                            dealerHand = DealerFunctions().hit(deck, dealerHand)
                            DealerFunctions().printDealerHand(dealerHand.getCards())

                        if GameFunctions().isBust(dealerHand):
                            print("Dealer busts! You win!")
                            balance += bet

                        else:
                            result, balance = GameFunctions().checkWinner(dealerHand, playerHand, balance, bet)
                            print(result)
                else:
                    for hand in playerHand.getCards():
                        hand = Hand(hand)
                        if GameFunctions().isBust(hand):
                            print("Bust! Dealer wins!")
                            balance -= bet
                        
                        else:
                            while GameFunctions().getHandValue(dealerHand) < 17:
                                dealerHand = DealerFunctions().hit(deck, dealerHand)
                                DealerFunctions().printDealerHand(dealerHand.getCards())

                            if GameFunctions().isBust(dealerHand):
                                print("Dealer busts! You win!")
                                balance += bet

                            else:
                                result, balance = GameFunctions().checkWinner(dealerHand, playerHand, balance, bet)
                                for e in result:
                                    print(e)

            print(f"Your balance: {balance}")

            if balance > 0:
                print("")
                playAgain = input("Do you want to play again? ")
                if playAgain == "no":
                    break

            else:
                print("\nYou have no more money to play.")
                break

        print("Thanks for playing!")