class Motocicleta:

    def __init__(self, viteza_curenta = 15, consum = 5):
        self.viteza_curenta = viteza_curenta
        self.consum = consum
        self.nr_pasageri = 1

    def adauga_pasager(self):
        self.nr_pasageri += 1

    def elimina_pasager(self):
        self.nr_pasageri -= 1

    def accelereaza(self):
        self.viteza_curenta += 15
        self.consum += 1

    def franeaza(self):
        if self.viteza_curenta:
            self.viteza_curenta -= 15
            self.consum -= 1
            if not self.viteza_curenta:
                self.consum = 0
        else:
            self.consum = 0