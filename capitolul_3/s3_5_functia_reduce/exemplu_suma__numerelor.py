from functools import reduce
def suma_numerelor(a, b):
    return a + b

lista_valori = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rez = reduce(suma_numerelor, lista_valori)
print(rez)