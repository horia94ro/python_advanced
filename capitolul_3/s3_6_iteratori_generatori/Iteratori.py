values = ["a", "b", "c"]
for val in values:
    print(val, end = " ")

print()
print(dir(values))

iter_values = iter(values) #echivalent cu values.__iter__()

print(dir(iter_values))

while True:
    try:
        val = next(iter_values)
        print(val)
    except StopIteration:
        print("Am terminat structura de date.")
        break