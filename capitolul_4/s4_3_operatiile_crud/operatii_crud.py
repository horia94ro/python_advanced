import mysql.connector

hostname = "127.0.0.1" #adresa IP de localhost
username = "root" #ne folosim de user-ul default de pe server
password = "" #nu avem parola configurată pe conexiune

con = mysql.connector.connect(host = hostname,
                              user = username,
                              password = password)

#Am realizat conexiunea inițială la serverul de baze de date

cursor = con.cursor()
query = "CREATE DATABASE IF NOT EXISTS clinica;" #Operația specifică pentru crearea unei noi baze de date
#partea de IF NOT EXISTS este opțională, pentru a nu avea erori dacă executăm aceeași operație de mai multe ori
cursor.execute(query)

select_db_query = "USE clinica;" #Trebuie să selectăm baza de date creată ca și implicită pentru a putea executa
#operații asupra ei
cursor.execute(select_db_query)

create_query = """
    CREATE TABLE IF NOT EXISTS pacient(
        id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        nume VARCHAR(50) NOT NULL,
        varsta INT NOT NULL
    );
"""

cursor.execute(create_query)
con.commit() #Pentru această operație este necesar și un commit, ca să ne asigurăm ca este executată

con.close() #Închidem conexiunea deja existentă

con = mysql.connector.connect(host = hostname,
                              user = username,
                              password = password,
                              database = "clinica") #Selectăm BD-ul dorit ca implicit

new_cursor = con.cursor()
# adaugare_pacienti = """
#     INSERT INTO pacient (nume, varsta)
#     VALUES
#     ('Laurentiu', 25),
#     ('Daniel', 23),
#     ('Miruna', 24),
#     ('Monica', 21),
#     ('Alex', 18)
# """
# new_cursor.execute(adaugare_pacienti)
# con.commit()
#

# extragere_pacienti = "SELECT * FROM pacient;"
# new_cursor.execute(extragere_pacienti)
# pacienti = new_cursor.fetchall()
#
# for pacient in pacienti:
#     print(pacient)

# actualizare_pacient = "UPDATE pacient SET varsta = 19 WHERE ID = 5;"
# #specificăm numele tabelei în care facem actualizarea, ce anume vrem să actualizăm și pentru cine
# new_cursor.execute(actualizare_pacient)
# con.commit()

# verificare_pacient = "SELECT nume, varsta FROM pacient WHERE ID = 5;"
# #extragem doar numele și vârsta pentru pacientul cu ID-ul 5, actualizat anterior
# new_cursor.execute(verificare_pacient)
# rezultat = new_cursor.fetchone()
# print(rezultat)

stergere_pacient = "DELETE FROM pacient WHERE ID = 4;"
new_cursor.execute(stergere_pacient)
con.commit()

verificare_pacienti = "SELECT * FROM pacient;"
new_cursor.execute(verificare_pacienti)
pacienti = new_cursor.fetchall()

for pacient in pacienti:
    print(pacient)