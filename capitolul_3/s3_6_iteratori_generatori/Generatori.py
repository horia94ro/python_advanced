def new_range(start, end):
    current_value = start
    while current_value <= end:
        yield current_value
        current_value += 1

my_gen = new_range(1, 5) #Tratăm generatorul definit mai sus ca pe un obiect de sine stătător.

print(next(my_gen)) #1

print(next(my_gen)) #2

print(next(my_gen)) #3