celsius = [26.2, 33.2, 29.3, 32.4]

def conversie_c_f(val):
    return 9/5 * val + 32

conv_lambda = lambda x: 9/5 * x + 32

# rez_f = map(conversie_c_f, celsius)
rez_f = map(conv_lambda, celsius)
for val in rez_f:
    print(val, end = ", ")


