from typing import final
class InstrumentMuzical(object):

    def __init__(self, material, pret):
        self.material = material
        self.pret = pret

    def scoate_sunet(self):
        print(f"Sunet specific de {self.material}")

    @final
    def deplaseaza(self):
        print("Deplasam instrumentul...")