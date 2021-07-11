from abc import ABC
from abc import abstractmethod


class Animal(ABC):

    _id_counter = 1

    def __init__(self, varsta, rasa, vaccinat):
        self.id = Animal._id_counter
        self.varsta = varsta
        self.rasa = rasa
        self.vaccinat = vaccinat
        Animal._id_counter += 1

    @abstractmethod
    def scoate_sunet(self):
        raise NotImplementedError("Metoda nu a fost inca suprascrisa!")

    @classmethod
    def mananca(cls):
        print("Am burtica plina!")