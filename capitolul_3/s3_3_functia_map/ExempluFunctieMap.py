def adunare(val):
    return val + 10

tuplu_date = (10, 20, 30, 40, 50)
rez = map(adunare, tuplu_date)
print(rez)

# for elem in rez:
#     print(elem, end = " ")

# print(tuple(rez))

# lambda_adunare = lambda val: val + 10
rez_lambda = map(lambda val: val + 10, tuplu_date)
for val in rez_lambda:
    print(val, end = " ")