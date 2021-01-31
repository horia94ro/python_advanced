class Pisica:

    def __init__(self, nume, varsta, greutate):
        self.nume = nume
        self.varsta = varsta
        self.greutate = greutate

    def spune_miau(self):
        print("Meow, numele meu este {}".format(self.nume))

leia = Pisica("Leia", 4, 5.6)
sheba = Pisica("Sheba", 3, 4.7)

leia.spune_miau()
sheba.spune_miau()