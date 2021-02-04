class Masina:
    def __init__(self, viteza_curenta = 0):
        self.viteza_curenta = viteza_curenta
        self.km_parcursi = 0
        self.timp_deplasare = 0

    def get_viteza(self):
        print("Deplasrea se face cu {} km/h".format(self.viteza_curenta))

    def accelereaza(self):
        self.viteza_curenta += 10

    def franeaza(self):
        if self.viteza_curenta:
            self.viteza_curenta -= 10
        else:
            pass

    def deplaseaza(self):
        self.km_parcursi += self.viteza_curenta
        self.timp_deplasare += 1

    def viteza_medie(self):
        if self.timp_deplasare:
            return self.km_parcursi / self.timp_deplasare
        else:
            pass