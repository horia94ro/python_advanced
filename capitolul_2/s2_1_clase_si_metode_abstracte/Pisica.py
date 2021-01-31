from capitolul_2.s2_1_clase_si_metode_abstracte.Animal import Animal

class Pisica(Animal):

    def __init__(self, nume, culoare):
        super().__init__(nume)
        self.culoare = culoare
        print("Am creat o pisica")

    def mananca(self):
        super().mananca() #avem posibilitatea de apela instrucțiunile din clasa parinte, chiar dacă acolo metoda era abstractă
        print("Pisica mananca mancare de pisici")


p1 = Pisica("MI", "GRI")
p1.mananca()
p1.vaneaza()