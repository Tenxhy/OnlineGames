import random as rand
from Utils import Suspance

suspance = Suspance()

class Simulazioni:
    def simulazione(risultatiGiocati, squadreOrdinate, moltiplicatori, contatore):
        golCasa = 0
        golTrasferta = 0
        
        if moltiplicatori[risultatiGiocati[contatore-1][0]-1][0] <= moltiplicatori[risultatiGiocati[contatore-1][0]-1][2]:
            ripetizioni = int(format(20/moltiplicatori[risultatiGiocati[contatore-1][0]-1][0], ".0f"))
            ripetizioni1 = int(20/moltiplicatori[risultatiGiocati[contatore-1][0]-1][2])

        else:
            ripetizioni1 = int(format(20/moltiplicatori[risultatiGiocati[contatore-1][0]-1][2], ".0f"))
            ripetizioni = int(20/moltiplicatori[risultatiGiocati[contatore-1][0]-1][0])

        for c in range(20):

            nrand = rand.randint(1,100)
            
            prob = []

            ripetizioni = int(format(20/moltiplicatori[risultatiGiocati[contatore-1][0]-1][0], ".0f"))

           
            for c in range(ripetizioni):
                
                prob.append(rand.randint(1,100))

            if nrand in prob:
                golCasa = golCasa+1
        
    
        for c in range(20):

            nrand = rand.randint(1,100)
            
            prob = []
            for c in range(ripetizioni1):
                prob.append(rand.randint(1,100))

            if nrand in prob:
                golTrasferta = golTrasferta+1

        return golCasa, golTrasferta

        