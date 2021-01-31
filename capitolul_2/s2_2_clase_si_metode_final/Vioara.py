from capitolul_2.s2_2_clase_si_metode_final.InstrumentMuzical import InstrumentMuzical
from typing import final

@final
class Vioara(InstrumentMuzical):

    def __init__(self, material, pret, nr_corzi):
        super().__init__(material, pret)
        self.nr_corzi = nr_corzi


    def scoate_sunet(self):
        super().scoate_sunet()
        print(f"Sunet specific de vioara cu {self.nr_corzi} corzi")

    #Metoda deplaseaza() este finala si NU ar trebui suprascrisa dar putem face asta oricum
    #PyCharm ne ofera doar un warning prin care indica aceasta incosecventa
    #Motivul <=> backwards compatibility

    def deplaseaza(self):
        pass

v1 = Vioara("lemn", 500, 5)
v1.scoate_sunet()
