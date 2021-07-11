from capitolul_2.s2_7_recap.Animal import Animal

class Pisica(Animal):

    def __init__(self, varsta, rasa, vaccinat, sterilizat):
        super().__init__(varsta, rasa, vaccinat)
        self.sterilizat = sterilizat

    def scoate_sunet(self):
        print(f"Meow! Am {self.varsta} ani si sunt de rasa {self.rasa}.")