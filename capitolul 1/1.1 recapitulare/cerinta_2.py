"""
CERINTA 2
Se citesc de la tastatura o serie de cuvinte, separate prin cate un spatiu.

Pe baza datelor citite, construiti un dictionare in care cheile sa fie reprezentate de cuvintele citite, iar valorile -
numarul de repetari al fiecarui cuvant in parte.
"""

mesaj = input("Introduceti tot textul pe o singura linie: ")
cuvintele = mesaj.split()

dictionar_aparitii = {}

#Alternativa 1
# for cuv in cuvintele:
#     if cuv in dictionar_aparitii:
#         dictionar_aparitii[cuv] += 1
#     else:
#         dictionar_aparitii[cuv] = 1
#         dictionar_aparitii.update({cuv:1})

#Alternativa 2
for cuv in cuvintele:
    if cuv not in dictionar_aparitii:
        dictionar_aparitii[cuv] = cuvintele.count(cuv)

print(dictionar_aparitii)