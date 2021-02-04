try:
    x = 0
    y = 10 / x
    print("A")
    my_list = [1, 2, 3]
    my_list[10] = 10
    print("B")
    my_dict = {'cheie_1': 100}
    my_dict['cheie_2'] += 1
    print("C")
    z = int("lala")
except IndexError:
    print("Te-ai lovit de un index inexistent.")
except KeyError:
    print("Ai incercat sa accesezi o cheie ce nu este prezenta in dictionar.")
except LookupError:
    print("Exceptie Lookup - care este peste IndexError/KeyError")
except ZeroDivisionError as e:
    print("Ai incercat sa imparti la 0, ba!", str(e))
except Exception as e: #excepții care nu se încadrează în niciuna din categoriile de mai sus
    print("Exceptie generala aruncata.")
    print(repr(e))
else:
    print("Bloc de instructiuni executat daca NU apar exceptii in cadrul TRY-ului.")
finally:
    print("Blocul de finally de la final.")