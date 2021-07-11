from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
engine = create_engine("mysql://root@localhost/clinica")
print(engine.connect())

class Doctor(Base):
    __tablename__ = 'doctor' #Numele tabelei așa cum va apărea în baza d date

    # declarăm în continuare atributele pe care dorim să le aibă clasa Doctor
    id = Column(Integer, primary_key = True)
    prenume = Column(String(25)) #Trebuie specificate lungimile maxime de caractere
    nume = Column(String(25))
    specializare = Column(String(10))

    def __repr__(self):
        return "Dr. {0} {1} este de specializare {2}".format(self.nume, self.prenume, self.specializare)
    #Folosirea lui __repr__ nu este obligatorie, dar vom vrea să avem un format frumos al datelor atunci când sunt
    #extrase din baza de date

print(Base.metadata.create_all(engine))

