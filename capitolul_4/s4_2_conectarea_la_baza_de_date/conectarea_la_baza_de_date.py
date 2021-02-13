import mysql.connector

try:
    conex = mysql.connector.connect(host = "127.0.0.1", #adresa se poate schimba dacă se lucreză cu baze de date remote
                                 user = "root", #numele de utilizator poate fi adaptat dacă se lucrează cu ceva custom
                                 password = "", #parola poate fi omisă ca și argument în cazul în care ea lipsește de pe autentificare
                                 port = 3306) #dacă portul folosi este cel default acest argument poate lipsi
                                 #totuși daca folosim altă valoare pentru port (ex: 33066) - ea trebuie specificată explicit
    my_cursor = conex.cursor()
    my_cursor.execute("CREATE DATABASE biblioteca2;")
    my_cursor.execute("SHOW DATABASES")
    for current_db in my_cursor:
        print(current_db)
except Exception as e:
    print(f"Exceptie aparuta la conectarea catre baza de date: {repr(e)}.")