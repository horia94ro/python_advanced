class Pisica:
    rasa = "birmaneza" #rasa va fi o zona de memorie statica, fiind declarata in afara init-ului/metodelor

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta


p1 = Pisica("Terra", 1)
p2 = Pisica("Leia", 4)
print(Pisica.rasa)
print(p1.rasa)
print(p2.rasa) #in urma executiei vom observa ca valoarea pentru zona de memorie rasa este aceeasi, indiferent de unde este apelata

p1.rasa = "siameza"
print(p1.rasa) #in aceasta situatie, rasa este tranformat intr-un atribut specific pentru instanta p1
print(Pisica.rasa) #dar zona de memorie statica ramane neafectata

Pisica.rasa = "scottish" #daca ne dorin sa modificam zona de memorie statica, trebuie sa o facem direct din numele clasei
print(p2.rasa)

print(id(Pisica.rasa))
print(id(p2.rasa)) #se poate verifica că zona de memorie este partajată de toate instanțele și cu ajutorul metodei id