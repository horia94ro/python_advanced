"""
Se citeste o valoare N de la tastatura. Ulterior se citesc, tot de la tastatura, N cuvinte.

Dupa terminarea citirii, afisati urmatoarele:

cuvintele citite, fara a afisa duplicate
toate cuvintele citite, dar scrise cu litere mari
doar cuvintele cu lungime para, chiar daca contin si duplicate
"""

count = int(input("Introduceti valoarea lui N: "))
cuv_unice = set()
toate_cuv = list()

for _ in range(count):
    cuv = input("Urmatorul cuvant: ")
    toate_cuv.append(cuv)
    cuv_unice.add(cuv)

print("Sirurile de caractere citite, fara duplicate:")
for cuv in cuv_unice:
    print(cuv, end = " ")

print("\n", "*" * 30, sep = "")

print("Toate sirurile de caractere, cu litere mari:")
for cuv in toate_cuv:
    print(cuv.upper(), end = " ")

print("\n", "*" * 30, sep = "")

print("Doar sirurile de caractere de lungime para:")
for cuv in toate_cuv:
    if len(cuv) % 2 == 0:
        print(cuv, end = " ")




