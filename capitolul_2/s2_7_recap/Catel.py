from capitolul_2.s2_7_recap.Animal import Animal


class Catel(Animal):

    def __init__(self, varsta, rasa, vaccinat):
        super().__init__(varsta, rasa, vaccinat)

    def scoate_sunet(self):
        print(f"Woof! Am {self.varsta} ani si sunt de rasa {self.rasa}.")