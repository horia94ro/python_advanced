from functools import reduce

def suma_numerelor(a, b):
    return a + b

suma_lambda = lambda x, y: x + y

lista_valori = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rez = reduce(suma_lambda, lista_valori)
print(rez)

