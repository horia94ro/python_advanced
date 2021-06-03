#Generator infinit

def generator_infinit(start):
    current_value = start
    while True:
        yield  current_value
        current_value += 1

values = generator_infinit(100)

for val in values:
    print(val)