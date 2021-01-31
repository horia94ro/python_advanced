from abc import ABC
from abc import abstractmethod

class Animal(ABC):

    def __init__(self, nume):
        self.nume = nume
        print("Am creat un animal")

    @abstractmethod
    def mananca(self):
        print("Metodele abstracte pot contine instructiuni.")


    def vaneaza(self):
        print("Clasele abstracte pot contine si metode concrete.")


# a1 = Animal() #această instanțiere nu este posibilă dacă clasa este abstractă și conține și metode abstracte
# a1.mananca()