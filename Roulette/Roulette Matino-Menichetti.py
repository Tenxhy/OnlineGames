import random as rand
import time
import sys

rosso = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
nero = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)

class Estraction():
    def __init__(self) -> None:
        pass
    
    def puntoSupspance(self, delay: float):
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(delay)

    def stringaSuspance(self, stringa: str, delay: float):
        for l in stringa:
            print(l, end="")
            time.sleep(delay)

    def estrai(self, num_estratto, colore_estratto, delay: float = 1):
        print("# La pallina è finita sul numero", end="")
        self.puntoSupspance(delay)
        print(f" {num_estratto} {colore_estratto}")

estraction = Estraction()

print("""
#####################################
#             BENVENUTO             #
#           ALLA ROULETTE           #
#    DEL CASINO MATINO-MENICHETTI   #
#####################################""")
print("#")
checkin = int(input("# Inserisca il suo budget di check-in\n# Budget:\t"))

while checkin > 0:

    print("""#\n# Su cosa vuole puntare? 
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

    ris = rand.randint(0,36)

    if ris in rosso:
        colore = "Rosso"
    elif ris in nero:
        colore = "Nero"
    else:
        colore = "Verde"
    
    imp = int()
    num = int()

    match scelta:
        
        case 1:
            num = int(input("# Ha scelto l'opzione numero secco!\n#\n# Su quale numero vuole puntare?\n# Puntata:\t"))
            print("#")
            while num<0 or num>36:
                num = int(input("# Inserisca un numero valido\t"))
            imp = int(input(f"# Inserisca quanto vuole puntare sul numero {num}\n# Puntata:\t"))
            while imp>checkin:
                imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\nInserisca un importo minore o uguale a {checkin}\n# Puntata:\t"))
            checkin = checkin-imp
            print("#")
            estraction.estrai(ris, colore, 1)

            if num == ris:
                print(f"# Lei ha vinto {imp*35} euro!\t")
                print(f"# Il suo portafoglio contiene ora {checkin+imp*35} euro\t", flush=True)
            else:
                print(f"# Lei ha perso!\t")
                print(f"# Il suo portafoglio contiene ora {checkin} euro\t", flush=True)

            time.sleep(4)
        
        case 2:
            print("# Ha scelto l'opzione numero pari!")
            print("#")
            imp = int(input(f"# Inserisca quanto vuole puntare\n# Puntata:\t"))
            while imp>checkin:
                imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\nInserisca un importo minore o uguale a {checkin}\n# Puntata:\t"))
            checkin = checkin-imp
            print("#")
            estraction.estrai(ris, colore, 1)

            if num%2 == 0:
                print(f"# Lei ha vinto {imp*2} euro!")
                print(f"# Il suo portafoglio contiene ora {checkin+imp*2} euro", flush=True)
            else:
                print(f"# Lei ha perso!")
                print(f"# Il suo portafoglio contiene ora {checkin} euro", flush=True)

            time.sleep(4)

        case 3:
            print("# Ha scelto l'opzione numero dispari!")
            print("#")
            imp = int(input(f"# Inserisca quanto vuole puntare\n# Puntata:\t"))
            while imp>checkin:
                imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\nInserisca un importo minore o uguale a {checkin}\n# Puntata:\t"))
            checkin = checkin-imp
            print("#")
            estraction.estrai(ris, colore, 1)

            if num%2 != 0:
                print(f"# Lei ha vinto {imp*2} euro!")
                print(f"# Il suo portafoglio contiene ora {checkin+imp*2} euro", flush=True)
            else:
                print(f"# Lei ha perso!")
                print(f"# Il suo portafoglio contiene ora {checkin} euro", flush=True)
            
            time.sleep(4)

        case 4:
            print("# Ha scelto l'opzione numero rosso!")
            print("#")
            imp = int(input(f"# Inserisca quanto vuole puntare\n# Puntata:\t"))
            while imp>checkin:
                imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\nInserisca un importo minore o uguale a {checkin}\n# Puntata:\t"))
            checkin = checkin-imp
            print("#")
            estraction.estrai(ris, colore, 1)
            
            if num in rosso:
                print(f"# Lei ha vinto {imp*2} euro!")
                print(f"# Il suo portafoglio contiene ora {checkin+imp*2} euro", flush=True)
            else:
                print(f"# Lei ha perso!")
                print(f"# Il suo portafoglio contiene ora {checkin} euro", flush=True)

            time.sleep(4)

        case 5:
            print("# Ha scelto l'opzione numero nero!")
            print("#")
            imp = int(input(f"# Inserisca quanto vuole puntare\n# Puntata:\t"))
            while imp>checkin:
                imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\nInserisca un importo minore o uguale a {checkin}\n# Puntata:\t"))
            checkin = checkin-imp
            print("#")
            estraction.estrai(ris, colore, 1)

            if num in nero:
                print(f"# Lei ha vinto {imp*2} euro!")
                print(f"# Il suo portafoglio contiene ora {checkin+imp*2} euro", flush=True)
            else:
                print(f"# Lei ha perso!")
                print(f"# Il suo portafoglio contiene ora {checkin} euro", flush=True)

            time.sleep(4)

        case 6:
            print("# Ha scelto l'opzione numero compreso tra 1 e 18!")
            print("#")
            imp = int(input(f"# Inserisca quanto vuole puntare\n# Puntata:\t"))
            while imp>checkin:
                imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\nInserisca un importo minore o uguale a {checkin}\n# Puntata:\t"))
            checkin = checkin-imp
            print("#")
            estraction.estrai(ris, colore, 1)

            if num>0 and num<19:
                print(f"# Lei ha vinto {imp*2} euro!")
                print(f"# Il suo portafoglio contiene ora {checkin+imp*2} euro", flush=True)
            else:
                print(f"# Lei ha perso!")
                print(f"# Il suo portafoglio contiene ora {checkin} euro", flush=True)

            time.sleep(4)

        case 7:
            print("# Ha scelto l'opzione numeri tra 19 e 36!")
            print("#")
            imp = int(input(f"# Inserisca quanto vuole puntare\n# Puntata:\t"))
            while imp>checkin:
                imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\nInserisca un importo minore o uguale a {checkin}\n# Puntata:\t"))
            checkin = checkin-imp
            print("#")
            estraction.estrai(ris, colore, 1)

            if num>18:
                print(f"# Lei ha vinto {imp*2} euro!")
                print(f"# Il suo portafoglio contiene ora {checkin+imp*2} euro", flush=True)
            else:
                print(f"# Lei ha perso!")
                print(f"# Il suo portafoglio contiene ora {checkin} euro", flush=True)

            time.sleep(4)

        case 8:
            print("# Ha scelto l'opzione prima dozzina di numeri!")
            print("#")
            imp = int(input(f"# Inserisca quanto vuole puntare\n# Puntata:\t"))
            while imp>checkin:
                imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\nInserisca un importo minore o uguale a {checkin}\n# Puntata:\t"))
            checkin = checkin-imp
            print("#")
            estraction.estrai(ris, colore, 1)

            if num>0 and num<13:
                print(f"# Lei ha vinto {imp*2} euro!")
                print(f"# Il suo portafoglio contiene ora {checkin+imp*3} euro", flush=True)
            else:
                print(f"# Lei ha perso!")
                print(f"# Il suo portafoglio contiene ora {checkin} euro", flush=True)

            time.sleep(4)

        case 9:
            print("# Ha scelto l'opzione seconda dozzina di numeri!")
            print("#")
            imp = int(input(f"# Inserisca quanto vuole puntare\n# Puntata:\t"))
            while imp>checkin:
                imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\nInserisca un importo minore o uguale a {checkin}\n# Puntata:\t"))
            checkin = checkin-imp
            print("#")
            estraction.estrai(ris, colore, 1)

            if num>12 and num<25:
                print(f"# Lei ha vinto {imp*2} euro!")
                print(f"# Il suo portafoglio contiene ora {checkin+imp*3} euro", flush=True)
            else:
                print(f"# Lei ha perso!")
                print(f"# Il suo portafoglio contiene ora {checkin} euro", flush=True)

            time.sleep(4) 

        case 10:
            print("# Ha scelto l'opzione terza dozzina di numeri!")
            print("#")
            imp = int(input(f"# Inserisca quanto vuole puntare\n# Puntata:\t"))
            while imp>checkin:
                imp = int(input(f"# Il valore inserito supera l'importo del suo portafoglio rimasto.\nInserisca un importo minore o uguale a {checkin}\n# Puntata:\t"))
            checkin = checkin-imp
            print("#")
            estraction.estrai(ris, colore, 1)

            if num>24:
                print(f"# Lei ha vinto {imp*2} euro!")
                print(f"# Il suo portafoglio contiene ora {checkin+imp*3} euro", flush=True)
            else:
                print(f"# Lei ha perso!")
                print(f"# Il suo portafoglio contiene ora {checkin} euro", flush=True)

            time.sleep(4)

print("#")
print("# Lei ha terminato tutto il budget. Arrivederci!")