from capitolul_4.s4_5_sqlalchemy.creare_tabela_sqlalchemy import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Instanțele clasei sunt create diferit de cele din OOP clasic
dr_house = Doctor(prenume = "Gregory", nume = "house", specializare = "cardio")
dr_grey = Doctor(prenume = "Meredith", nume = "Grey", specializare = "general")
session.add(dr_house)
session.add(dr_grey)
# Fara a executa operația de commit, instanțele vor fi disponibile strict la nivel local
session.commit()

doctori = session.query(Doctor).order_by(Doctor.id)
for doctor in doctori:
    print(doctor)