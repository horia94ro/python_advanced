class NewRange:

    def __init__(self, start, end):
        self.current_value = start
        self.end = end

#Pentru a transforma instanțele clasei în unele iterabile, vom avea nevoie să folosim metoda __iter__().
    def __iter__(self):
        return self

#Returnăm instanța în sine întrucât mai departe vom suprascrie și metoda __next__(). Făcând acest lucru, vom putea spune despre clasa noastră că este și iterabilă și un iterator.

    def __next__(self):
    #Începem prin a verifica dacă am ajuns la finalul intervalului pe care vrem să îl parcurgem
        if self.current_value >= self.end:
            raise StopIteration
        value = self.current_value
        self.current_value += 1
#self.value va fi responsabil cu a reține starea curentă a obiectului, știind practic care este următoarea valoare ce trebuie returnată.
        return value

nr1 = NewRange(1, 5)
for val in nr1:
    print(val, end = " ")

nr2 = NewRange(2, 10)
print(next(nr2)) #2
print(next(nr2)) #3
print(next(nr2)) #4