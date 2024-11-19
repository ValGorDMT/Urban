def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 2, 3]
values_dict = {'a' : 1, 'b' : 2, 'c' : 3}

print_params(values_list)
print_params(*values_list)
print_params(values_dict)
print_params(**values_dict)

values_list2 = [1, 2]

print_params(*values_list2, 3)