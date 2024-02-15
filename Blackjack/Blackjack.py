import random as rand
from colorama import Fore, Back, Style
import yaml
from Cards import Deck
from Cards import Value

deck = Deck(4)

class Blackjack():

    def play(self):

        print("""
#################################################################
#\t\t   BLACKJACK MATINO MENICHETTI      \t\t#
#################################################################""".strip())
        print("#")

        budget = float(input("# Benvenuto al nostro programma di blackjack. Inserisca l'importo della ricarica: "))

        while not(budget > 0 and budget < 10000):
            budget = float(input("# Inserisca una cifra compresa tra 0 e 10000: "))

        while budget > 0:
            bet = float(input("# Inserisca la sua puntata: "))

            while bet < 0 or bet > budget:
                bet = float(input("# Inserisca la sua puntata: "))
            
            drawn_cards = deck.drawCards(2)

            if not drawn_cards is None:
                first_card, second_card = drawn_cards
            else:
                print("# Mazzo esaurito")
                break
            
            handvalue = first_card.getValue().value + second_card.getValue().value

            print("# La sua mano è:", str(first_card), str(second_card))
            print("# Il valore della sua mano è:", handvalue)

            first_dealer_card = deck.drawCard()
            second_dealer_card = deck.drawCard()

            dealer_handvalue = first_dealer_card.getValue().value

            print("# La mano del banco è:", str(first_dealer_card))
            print("# Il valore della mano del banco è:", dealer_handvalue)

            if handvalue == 21:
                print("# Blackjack!")

            elif first_card.getValue() == second_card.getValue():
                choice = int(input("# Scelga cosa vuole fare:\n# 1. Stare\n# 2. Chiamare carta\n# 3. Dividere \n# 4. Raddoppiare"))

                match choice:

                    case 1: 
                        pass

                    case 2:
                        card = deck.drawCard()
                        print("#", str(card))

                        handvalue = handvalue + card.getValue().value

                        print("# Il valore della sua mano è:", handvalue)

                    case 3:
                        card1, card2 = deck.drawCards(2)



            else:
                choice = int(input("# Scelga cosa vuole fare:\n# 1. Stare\n# 2. Chiamare carta\n# 3. Raddoppiare\n# "))

        print("#")
