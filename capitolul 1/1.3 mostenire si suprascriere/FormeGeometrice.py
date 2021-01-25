class FormaGeometrica:

    def calculeaza_arie(self):
        raise NotImplementedError("Metoda de calcul arie trebuie supascrisa")

class Triunghi(FormaGeometrica):

    def __init__(self, baza, inaltime):
        self.baza = baza
        self.inaltime = inaltime

    def calculeaza_arie(self):
        arie = self.baza * self.inaltime / 2
        return arie


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.latura = latura

    def calculeaza_arie(self):
        return self.latura ** 2

    def calculeaza_petrimetru(self):
        return self.latura * 4


