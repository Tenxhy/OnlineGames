import random as rand
from colorama import Fore, Back, Style
import yaml
import os
from Simulazioni import Simulazioni
from Utils import Suspance

class Virtuali():
    def __init__(self) -> None:
        self.suspance = Suspance()

        with open(os.path.dirname(__file__) + r'\configs\config.yml', 'r') as file:
            config = yaml.safe_load(file)

        self.nomiSquadre = config["nomi_squadre"]
        self.vittorie = config["vittorie"]
        self.partiteGiocate = config["partite_giocate"]
        self.squadre = {}
    
    def play(self):
        squadre = self.squadre

        class Squadra():

            def __init__(self, name, vittorie, partite_giocate, rate = None, estratta = False):
                self.name = name
                self.vittorie = vittorie
                self.partite_giocate = partite_giocate
                self.winrate = vittorie/partite_giocate
                self.rate = rate
                self.estratta = estratta
        
        for i in range(len(self.nomiSquadre)):
            detailedSquadra = Squadra(self.nomiSquadre[i], self.vittorie[i], self.partiteGiocate[i])

            squadre.update({self.nomiSquadre[i]: detailedSquadra})


        print("""
#################################################################
#\t\t            VIRTUALI               \t\t#
#################################################################""".strip())
        print("#")

        budget = float(input("# Benvenuto al nostro programma di virtuali calcistiche. Inserisca l'importo della ricarica  "))

        while not(budget > 0 and budget < 10000):
            budget = float(input("# Inserisca una cifra compresa tra 0 e 10000:  "))

        print("#")
        squadreOrdinate = []
        moltiplicatori = []

        for i in range(10):
            squadreEstratte = []
            for c in range(2):
                randSquadra = squadre[tuple(squadre.keys())[rand.randint(0, len(squadre.keys())-1)]]
                while randSquadra.estratta:
                    randSquadra = squadre[tuple(squadre.keys())[rand.randint(0, len(squadre.keys())-1)]]
                randSquadra.estratta = True
                squadre.update({randSquadra.name: randSquadra})
                squadreEstratte.append(randSquadra)
            
            print(f"# {i+1}.\t", "\033[1m" + squadreEstratte[0].name, end="   -   ")
            print(squadreEstratte[1].name + "\033[0m")

            squadreEstratte[0].rate = float(format(0.75/squadreEstratte[0].winrate, ".2f"))
            squadreEstratte[1].rate = float(format(1/squadreEstratte[1].winrate, ".2f"))

            if squadreEstratte[1].rate - squadreEstratte[0].rate > 1.5:
                squadreEstratte[0].rate = float(format(squadreEstratte[0].rate - 0.2, ".2f"))

            pareggio = float(format((squadreEstratte[0].rate+squadreEstratte[1].rate)/2+0.5, ".2f"))

            if pareggio > 4:
                pareggio = float(format(pareggio - 1))

            elif pareggio > 3.50:
                pareggio = float(format(pareggio - 0.5))

            moltiplicatori.append((squadreEstratte[0].rate, pareggio, squadreEstratte[1].rate))
            squadreOrdinate.append(squadreEstratte[0].name + " - " + squadreEstratte[1].name)
            
            print("#\t", squadreEstratte[0].rate, "  ", pareggio , "   ", squadreEstratte[1].rate)
            print("#")

        npartite = int(input("# Inserisca il numero di partite che vuole giocare:  "))
        print("#")

        while npartite < 1 or npartite > 10:
            npartite = int(input("# Inserisca un numero valido:  "))

        risultatiGiocati = []
        quota = 1
        partiteNonValide = []

        for c in range(npartite):

            partiteSchedina = int(input("# Inserisca il numero della partita che vuoi giocare:  "))

            while partiteSchedina in partiteNonValide or not (partiteSchedina > 0 and partiteSchedina < 11):
                partiteSchedina = int(input("# Inserisca una partita valida e che non ha già giocato:  "))

            print("#")
            print(f"# Ha scelto la partita {squadreOrdinate[partiteSchedina-1]}")
            print("#")
            print("#", end=" ")

            for moltiplicatore in moltiplicatori[partiteSchedina-1]:
                print(moltiplicatore, end= " ")
            print("")
            print("#")
            unoxdue = input("# Inserisca che risultato vuoi giocare 1 X 2:  ")

            while not unoxdue in ["1", "X", "2"]:
                unoxdue = input("# Inserisca un risultato valido! 1 X 2:  ")
            
            match unoxdue.upper():
                case "1":
                    quota = format(float(quota)*moltiplicatori[partiteSchedina-1][0],".2f")
                case "X":
                    quota = format(float(quota)*moltiplicatori[partiteSchedina-1][1],".2f")
                case "2":
                    quota = format(float(quota)*moltiplicatori[partiteSchedina-1][2],".2f")
            
            risultatiGiocati.append((partiteSchedina, unoxdue))
            partiteNonValide.append(partiteSchedina)
            print("# La quota totale ora è", quota)
            print("#")

        importo = float(input("# Inserisca l'importo della virtuale:  "))

        while not (importo > 0 and importo < 1000):
            importo = float(input("# L'importo deve essere compreso tra 1 e 1000:  "))

        while importo > budget:
            importo = float(input(f"# L'importo inserito supera il suo budget di {budget} euro:  "))

        budget = budget - importo

        vincitaPotenziale = format(float(float(quota)*importo), '.2f')
        print(f"# La vincita potenziale è di {vincitaPotenziale}" + " euro ")
        print("#")
        print("#")
        print("# Simulazione delle partite", end = "")
        self.suspance.puntoSupspance(2)
        print("")

        risultatiFinali = []
        contatore = 0
        risultatiGiocatiDict = dict(risultatiGiocati)
        reordered_dict = {k: risultatiGiocatiDict[k] for k in range(11) if k in risultatiGiocatiDict}
        check = True
        for partite in range(10):

            if partite+1 in reordered_dict.keys():

                golCasa, golTrasferta = Simulazioni.simulazione(risultatiGiocati, squadreOrdinate, moltiplicatori, contatore)

                if golCasa > golTrasferta:
                    risultatiFinali.append("1")

                elif golCasa == golTrasferta:
                    risultatiFinali.append("X")

                elif golCasa < golTrasferta:
                    risultatiFinali.append("2")
                contatore = contatore+1

                print("#")

                if risultatiFinali[contatore-1] == reordered_dict[partite+1]:
                    print(Fore.LIGHTYELLOW_EX + "# Il risultato di",squadreOrdinate[partite], " è " + Style.RESET_ALL, Back.GREEN, golCasa, "-", str(golTrasferta), Style.RESET_ALL)

                else:
                    print(Fore.LIGHTYELLOW_EX + "# Il risultato di",squadreOrdinate[partite], " è " + Style.RESET_ALL, Back.RED, golCasa, "-", str(golTrasferta), Style.RESET_ALL)
                    check = False
                
        if check:
            print("# Lei ha appena vinto! Il checkout è di " + Fore.GREEN, str(vincitaPotenziale) + " euro", Style.RESET_ALL)

            budget = budget + float(vincitaPotenziale)

        else:
            print("# Lei ha appena perso! La perdita è di "+ Fore.RED, str(importo) + " euro", Style.RESET_ALL)

        scelta = int(input(f"# Il suo budget attuale è di {budget} euro. Per continuare a giocare prema 1, per smettere prema qualsiasi altro tasto: "))
            
        if scelta == 1:
            self.play()