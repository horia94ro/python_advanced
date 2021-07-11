"""
Se va realiza un program pentru gestionarea unui centru de adăpost și adopții al animalelor.
Despre fiecare animal în parte se cunosc următoarele informații: vârsta, rasa și daca a fost vaccinat sau nu.

În cadrul adăpostului pot fi găzduite sau adoptate pisici și căței. O parte dintre animalele ce se află în adăpost
trebuie să fie sterilizate înainte de a fi date spre adopție. În cazul acestui adăpost, doar
despre pisici trebuie știut dacă sunt sterilizate sau nu.

Fiecare animal găzduit în cadrul adăpostului trebuie să știe să scoată un sunet specific - ”Woof” sau ”Meow!”,
împreuna cu vârsta și rasa sa. De asemenea toate animalele trebuie să mănânce și vor afișa un mesaj general
după ce sunt hrănite - ”Am burtica plină!”.

Adăpostul poate găzdui la un moment dat, cel mult 30 de animale, atât pisici cât și căței.

Aplicația lucrează cu un singur centru de adăpost-adopții și are următoarele funcționalități:

- adăugare animal
- adopție animal
- afișare animale
- afișare specifică doar a unui tip de animale

Pentru a executa aceste funcționalități, aplicația primește de la tastatură următoarele comenzi:

- adauga_catel <varsta> <rasa> <vaccinat>
- adauga_pisica <varsta> <rasa> <vaccinat> <sterilizat>
- adopta_animal <id>
- exit
- afiseaza
- afiseaza <tip_animal>
"""
from capitolul_2.s2_7_recap.Adapost import Adapost
from capitolul_2.s2_7_recap.Catel import Catel
from capitolul_2.s2_7_recap.Pisica import Pisica


if __name__ == "__main__":
    adapost_local = Adapost()
    while True:
        line = input("Introduceti o noua comanda: ")
        cmd = line.split()
        if cmd[0] == "exit":
            print("Aplicatia se va inchide...")
            break
        elif cmd[0] == "afiseaza":
            if len(cmd) == 1:
                adapost_local.afisare_animale()
            else:
                tip_animal = cmd[1]
                adapost_local.afisare_specifica(tip_animal)
        elif cmd[0] == "adauga_catel":
            varsta = int(cmd[1])
            rasa = cmd[2]
            vaccinat = cmd[3]
            c = Catel(varsta, rasa, vaccinat)
            adapost_local.adauga_animal(c)
        elif cmd[0] == "adauga_pisica":
            varsta = int(cmd[1])
            rasa = cmd[2]
            vaccinat = cmd[3]
            sterilizat = cmd[4]
            p = Pisica(varsta, rasa, vaccinat, sterilizat)
            adapost_local.adauga_animal(p)
        elif cmd[0] == "adopta_animal":
            id_adoptat = int(cmd[1])
            adapost_local.adoptie_animal(id_adoptat)