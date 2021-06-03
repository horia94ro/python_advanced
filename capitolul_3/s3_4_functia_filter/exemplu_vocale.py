def filtrare_vocale(var):
    vocale = ['a', 'e', 'i', 'o', 'u']
    if var in vocale:
        return True
    else: return False


secventa = "Acesta este un text din care vom extrage vocalele."
rezultat = filter(filtrare_vocale, secventa) #Funcția de filtrare este pasată sub formă de obiect, nu este apelată
for c in rezultat: #Rezultatul este tot un obiect iterabil
    print(c, end = " ")
