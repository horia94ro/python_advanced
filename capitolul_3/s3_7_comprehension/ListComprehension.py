#Exemplul 1: Ne dorim să copiem valorile dintr-o listă existentă în una nouă

#Abordarea clasică este de a itera prin elementele existente și a le copia unul câte unul în noua listă
valori = ["a", "b", "c", "d", "e", "z"]
lista_noua = list()
for val in valori:
    lista_noua.append(val)

print(lista_noua)

#Pe de altă parte, dacă ne folosim de list comprehension, liniile de mai sus se pot rezuma la
lista_noua = [val for val in valori]
print(lista_noua)

#Practic, putem observa că ne folosim în continuare de for, dar într-un mod prescurtat.

#Exemplul 2: Avem o listă ce conține valori numerice întregi. Vrem să generăm o nouă
#listă, ce conține pătratul valorilor din lista inițială

lista_numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Abordare clasică:
lista_patrate = list()
for nr in lista_numere:
    patrat = nr ** 2
    lista_patrate.append(patrat)

#Echivalent, cu ajutorul list comprehension
lista_patrate = [nr ** 2 for nr in lista_numere]
print(lista_patrate)

#Alternativă cu map și lambda - mai dificilă de citit și înțeles
lista_patrate = map(lambda nr : nr ** 2, lista_numere)
print(list(lista_patrate))

#Exemplul 3: Plecând de la o colecție de valori numerice definite într-o listă și folosindu-vă de list comprehension,
#generați o nouă listă care să conțină doar valorile pare din cea inițială.

valori = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista_finala = list()
#Abordare clasică
for val in valori:
    if val % 2 == 0:
        lista_finala.append(val)
print(lista_finala)

#Echivalent cu
lista_finala = [val for val in valori if val % 2 == 0]
print(lista_finala)
