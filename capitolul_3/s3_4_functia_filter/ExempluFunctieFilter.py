def extragere_vocale(var):
    vocale = ['a', 'e', 'i', 'o', 'u']
    if var.lower() in vocale:
        return True
    else:
        return False

extragere_lambda = lambda var: var.lower() in ['a', 'e', 'i', 'o', 'u']


secventa = "Acesta este un text mai lung din care vreau sa extrag vocalele."
rez = filter(extragere_lambda, secventa)
# print(rez)
for letter in rez:
    print(letter, end = ", ")