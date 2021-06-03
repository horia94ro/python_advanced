def adunare(val):
    return val + 10


tuplu_date = (10, 20, 30, 40)
result = map(adunare, tuplu_date)
#Se poate observa că funcția de adunare este dată ca argument, fără a face un apel concret al ei
print(result) #Printarea rezultatului va fi un obiect iterabil
print(list(result)) #Dacă dorim să extragem datele cu totul sub formă de listă

result = map(adunare, tuplu_date) #Mai apelăm o dată funcția map cu aceeași parametrii întrucât am epuizat obiectele din rezultatul inițial deja
for elem in result:
    print(elem, end = " ") #Dacă dorim să extragem rezultatele pe rând