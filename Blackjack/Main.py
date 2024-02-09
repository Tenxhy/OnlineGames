import random as rand
from colorama import Fore, Back, Style
import yaml
from Cards import Deck
from Cards import Value

deck = Deck(2)

class BlackjackMain():

    def start(self):

        print("""
#################################################################
#\t\t   BLACKJACK MATINO MENICHETTI      \t\t#
#################################################################""".strip())
        print("#")

        budget = float(input("# Benvenuto al nostro programma di blackjack. Inserisca l'importo della ricarica  "))

        while not(budget > 0 and budget < 10000):
            budget = float(input("# Inserisca una cifra compresa tra 0 e 10000:  "))

        while budget > 0:
            bet = float(input("# Inserisca la sua puntata: "))

            while bet < 0 or bet > budget:
                bet = float(input("# Inserisca la sua puntata: "))
        
            first_card = deck.drawCard()
            second_card = deck.drawCard()
            
            handvalue = first_card.getValue().value + second_card.getValue().value

            print("# La sua mano e':", first_card.getFormattedName(), second_card.getFormattedName())
            print("# Il valore della sua mano e':", handvalue)

            first_dealer_card = deck.drawCard()
            second_dealer_card = deck.drawCard()

            dealer_handvalue = first_dealer_card.getValue().value

            print("# La mano del banco e':", first_dealer_card.getFormattedName())
            print("# Il valore della mano del banco e':", dealer_handvalue)

            if handvalue == 21:
                print("# Blackjack!")

            elif first_card.getValue() == second_card.getValue():
                choice = int(input("# Scelga cosa vuole fare:\n# 1. Stare\n# 2. Chiamare carta\n# 3. Dividere \n# 4. Raddoppiare"))

                match choice:

                    case 1: 
                        pass

                    case 2:
                        card = deck.drawCard()
                        print("#", card.getFormattedName)

                        handvalue = handvalue + card.getValue().value

                        print("# Il valore della sua mano e':", handvalue)

                    case 3:
                        card1 = deck.drawCard()
                        card2 = deck.drawCard()



            else:
                choice = int(input("# Scelga cosa vuole fare:\n# 1. Stare\n# 2. Chiamare carta\n# 3. Raddoppiare"))


        print("#")
