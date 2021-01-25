class Animal:

    def __init__(self, nume):
        self.nume = nume

    def doarme(self):
        print("Animalul {} doarme".format(self.nume))

class Catel(Animal):

    def __init__(self, nume, dresat):
        super().__init__(nume)
        self.dresat = dresat

    def latra(self):
        print("Catelul {} latra.".format(self.nume))

class Pisica(Animal):

    def __init__(self, nume):
        super().__init__(nume)

    def spune_miau(self):
        print("Pisica {} miauna".format(self.nume))

    def toarce(self):
        print("Pisica {} toarce".format(self.nume))