class NotEnoughMoneyException(Exception):

    def __init__(self, diferenta):
        super().__init__(f"Nu aveti suficienti bani in cont! Va lipsesc {diferenta}")

class Client(object):

    def __init__(self, cnp, fonduri_curente = 0):
        self.cnp = cnp
        self.fonduri_curente = fonduri_curente

    def alimenteaza_cont(self, suma_depusa):
        if suma_depusa < 0:
            raise ValueError("Nu puteti depune sume negative!")
        self.fonduri_curente += suma_depusa


    def retrage_suma(self, suma_retrasa):
        if suma_retrasa > self.fonduri_curente:
            diferenta = suma_retrasa - self.fonduri_curente
            raise NotEnoughMoneyException(diferenta)
        elif suma_retrasa == self.fonduri_curente:
            print("Ti-ai retras toti banii! Mare atentie!")
            return 0
        elif suma_retrasa < self.fonduri_curente:
            self.fonduri_curente -= suma_retrasa
            return self.fonduri_curente

