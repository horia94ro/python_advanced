def ridicare_la_putere(exp):
    def ridicare_valoare_la_putere(val):
        return pow(val, exp)
    return ridicare_valoare_la_putere

patrat = ridicare_la_putere(2)
cub = ridicare_la_putere(3)

print(patrat(7)) # va afișa 49
print(cub(7)) #va afișa 343