import time

def my_timer(func):
    def wrapper_func(*args, **kwargs):
        t1 = time.time()
        rezultat = (func(*args, **kwargs))
        t2 = time.time()
        print(f"Executia functiei {func.__name__} a durat {round(t2 - t1, 2)} secunde")
        return rezultat
    return wrapper_func

@my_timer
def suma_numerelor(val):
    suma = 0
    for i in range(0, val):
        suma += i
    return suma

print(suma_numerelor(10000000))