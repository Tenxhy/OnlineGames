import time

class Delay():
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
        return num_estratto, colore_estratto
