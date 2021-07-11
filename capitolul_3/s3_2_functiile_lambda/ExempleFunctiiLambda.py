def my_function(x):
    return x ** 2

my_lambda = lambda x : x ** 2
# print(my_lambda)
# print(my_lambda(7))

my_sec_lambda = lambda x, y, z : x + y + z
print(my_sec_lambda(10, 20, 30))
print(my_sec_lambda(z = 5, y = 10, x = 7))

my_print_lambda = lambda : print("HELLO WORLD")
my_print_lambda()

