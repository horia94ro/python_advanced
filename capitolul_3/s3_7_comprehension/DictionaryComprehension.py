# nume_complete = [('Ionescu', 'Andrei'), ('Popescu', 'George'), ('Spilca', 'Laurentiu'), ('Dumitru', 'Alin')]
#
# dictionar_nume = dict()
#
# for nume, prenume in nume_complete:
#     dictionar_nume[nume] = prenume
#
# print(dictionar_nume)
#
# dictionar_nume = {nume : prenume for nume, prenume in nume_complete}
# print(dictionar_nume)


an_masini = ((1974, 'Enzo'), (1984, 'Spider'), (1996, 'California'), (1985, 'Superamerica'),
             (1966, 'GTS'), (2001, 'Berlinetta'))

dictionar_masini = dict()

for an, model in an_masini:
    if an >= 1980:
        dictionar_masini[an] = model

print(dictionar_masini)

dictionar_masini = {an : model for an, model in an_masini if an >= 1980}
print(dictionar_masini)