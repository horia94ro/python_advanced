class Triunghi:

    def __init__(self, baza, inaltime):
        self.baza = baza
        self.inaltime = inaltime

    def calculeaza_arie(self):
        "Vom considera latura 3 ca fiind baza in cazul de fata"
        arie = self.baza * self.inaltime / 2
        return arie


t1 = Triunghi(10, 11)
print(t1.calculeaza_arie())

