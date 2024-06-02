import time
from Utils.Delay import Delay
import time
import random

estraction = Delay()

class Roulette:
    def __init__(self):
        self.rosso = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
        self.nero = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)
        self.checkin = int(input("""
#################################################################
#\t\t            ROULETTE            \t\t#
#################################################################
#
# Inserisca il suo budget di check-in\n# Budget:\t"""))

    def _get_bet(self, message: str = "# Inserisca quanto vuole puntare\n# Puntata:\t"):
        imp = int(input(message))
        while imp > self.checkin:
            imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\n# Inserisca un importo minore o uguale a {self.checkin}\n# Puntata:\t"))
        self.checkin -= imp
        print("#")
        return imp

    def _estrai(self):
        ris = random.randint(0,36)
        if ris in self.rosso:
            colore = "Rosso"
        elif ris in self.nero:
            colore = "Nero"
        else:
            colore = "Verde"
        return ris, colore

    def _esito(self, vittoria: bool = True, valore: float = None,):
        if vittoria and valore != None:
            self.checkin += valore
            print(f"# Lei ha vinto {valore} euro!")
            print(f"# Il suo portafoglio contiene ora {self.checkin} euro\t", flush=True)
        else:
            print(f"# Lei ha perso!\t")
            if self.checkin <= 0:
                print("# Il suo portafoglio è vuoto. Grazie per aver giocato!")
            else:
                print(f"# Il suo portafoglio contiene ora {self.checkin} euro\t", flush=True)

    def _numero_secco(self):
        num = int(input("# Ha scelto l'opzione numero secco!\n#\n# Su quale numero vuole puntare?\n# Numero:\t"))
        print("#")
        while num < 0 or num > 36:
            num = int(input("# Inserisca un numero valido\t"))
        imp = self._get_bet()
        n_estr, col_estr = self._estrai()
        ris, _ = estraction.estrai(n_estr, col_estr)

        if num == ris:
            self._esito(True, imp*35)
        else:
            self._esito(False)

    def _numero_pari(self):
        print("# Ha scelto l'opzione numero pari!")
        print("#")
        imp = self._get_bet()
        n_estr, col_estr = self._estrai()
        ris, _ = estraction.estrai(n_estr, col_estr)

        if ris % 2 == 0:
            self._esito(True, imp*2)
        else:
            self._esito(False)

    def _numero_dispari(self):
        print("# Ha scelto l'opzione numero dispari!")
        print("#")
        imp = self._get_bet()
        n_estr, col_estr = self._estrai()
        ris, _ = estraction.estrai(n_estr, col_estr)

        if ris % 2 != 0:
            self._esito(True, imp*2)
        else:
            self._esito(False)

    def _numero_rosso(self):
        print("# Ha scelto l'opzione numero rosso!")
        print("#")
        imp = self._get_bet()
        n_estr, col_estr = self._estrai()
        ris, colore = estraction.estrai(n_estr, col_estr)
        
        if colore == "Rosso":
            self._esito(True, imp*2)
        else:
            self._esito(False)

    def _numero_nero(self):
        print("# Ha scelto l'opzione numero nero!")
        print("#")
        imp = self._get_bet()
        n_estr, col_estr = self._estrai()
        ris, colore = estraction.estrai(n_estr, col_estr)
        
        if colore == "Nero":
            self._esito(True, imp*2)
        else:
            self._esito(False)

    def _num_1_18(self):
        print("# Ha scelto l'opzione numero compreso tra 1 e 18!")
        print("#")
        imp = self._get_bet()
        n_estr, col_estr = self._estrai()
        ris, _ = estraction.estrai(n_estr, col_estr)

        if ris > 0 and ris < 19:
            self._esito(True, imp*2)
        else:
            self._esito(False)

    def _num_19_36(self):
        print("# Ha scelto l'opzione numeri tra 19 e 36!")
        print("#")
        imp = self._get_bet()
        n_estr, col_estr = self._estrai()
        ris, _ = estraction.estrai(n_estr, col_estr)

        if ris > 18:
            self._esito(True, imp*2)
        else:
            self._esito(False)

    def _prima_12(self):
        print("# Ha scelto l'opzione prima dozzina di numeri!")
        print("#")
        imp = self._get_bet()
        n_estr, col_estr = self._estrai()
        ris, _ = estraction.estrai(n_estr, col_estr)

        if ris > 0 and ris < 13:
            self._esito(True, imp*3)
        else:
            self._esito(False)

    def _seconda_12(self):
        print("# Ha scelto l'opzione seconda dozzina di numeri!")
        print("#")
        imp = self._get_bet()
        n_estr, col_estr = self._estrai()
        ris, _ = estraction.estrai(n_estr, col_estr)

        if ris > 12 and ris < 25:
            self._esito(True, imp*3)
        else:
            self._esito(False)

    def _terza_12(self):
        print("# Ha scelto l'opzione terza dozzina di numeri!")
        print("#")
        imp = self._get_bet()
        n_estr, col_estr = self._estrai()
        ris, _ = estraction.estrai(n_estr, col_estr)

        if ris>24:
            self._esito(True, imp*3)
        else:
            self._esito(False)
    
    def play(self):
        print("#")

        while self.checkin > 0:
            print("""#
# Su cosa vuole puntare?\n#
# Ecco le diverse opzioni:\n#
#\t1. Numero secco
#\t2. Numero pari
#\t3. Numero dispari
#\t4. Numero rosso
#\t5. Numero nero
#\t6. Numeri da 1 a 18
#\t7. Numeri da 19 a 36
#\t8. Prima dozzina di numeri
#\t9. Seconda dozzina di numeri
#\t10. Terza dozzina di numeri\n#""")

            scelta = int()

            while scelta < 1 or scelta > 10:
                scelta = int(input("# Inserisca uno dei numeri riportati qua sopra\n# Scelta:\t"))

            match scelta:
                case 1:
                    self._numero_secco()
                case 2:
                    self._numero_pari()
                case 3:
                    self._numero_dispari()
                case 4:
                    self._numero_rosso()
                case 5:
                    self._numero_nero()
                case 6:
                    self._num_1_18()
                case 7:
                    self._num_19_36()
                case 8:
                    self._prima_12()
                case 9:
                    self._seconda_12()
                case 10:
                    self._terza_12()
            
            time.sleep(2)
