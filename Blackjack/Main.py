import random as rand
from colorama import Fore, Back, Style
import yaml
from Cards import Deck

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


        card = deck.drawCard()
        print("#", card.getFormattedName())

 
        print("#")
