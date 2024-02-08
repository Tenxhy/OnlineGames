import time

class Suspance():
    
    def puntoSupspance(self, delay: float):
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(delay)

    def stringaSuspance(self, stringa: str, delay: float):
        for l in stringa:
            print(l, end="")
            time.sleep(delay)

