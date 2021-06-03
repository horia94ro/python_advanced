"""
Exercițiul 1:

Avem definită o listă ce conține o serie de șiruri de caractere, scrise cu litere mici.
Pe baza acesteia, generați o altă listă care să conțină aceleași șiruri de caractere,
dar scrise cu litere mari și numai dacă au număr impar de caractere.

Rezolvați cerința atât într-un mod clasic, cu ajutorul for, dar și cu ajutorul list comprehension.

"""

lista_initiala = ['siruri', 'clasa', 'cana', 'lungime', 'controale', 'pisica', 'catel']
lista_rez = list()

#Abordare clasică
for cuv in lista_initiala:
    if len(cuv) % 2 == 1:
        lista_rez.append(cuv.upper())

print(lista_rez)

#Rezolvare echivalentă, cu list comprehension
lista_rez = [cuv.upper() for cuv in lista_initiala if len(cuv) % 2 == 1]
print(lista_rez)
"""
Exercițiul 2:

Plecând de la următoarele două structuri:

sir = "abcd"
val = "0123"

generați toate secvențele de tupluri care să conțină o literă din prima structură și o cifă din a doua structură:

[(a, 1), (a, 2), (a, 3), (b, 1), (b, 2)... (d, 2), (d, 3)]

Rezolvați cerința atât într-un mod clasic, cu ajutorul for, dar și cu ajutorul list comprehension.
"""


sir = "abcd"
val = "0123"
rez = list()
#Abordare clasică
for let in sir:
    for num in val:
        rez.append((let, num))

print(rez)

#Rezolvare echivalentă, cu list comprehension
rez = [(litera, cifra) for litera in sir for cifra in val]
print(rez)

