print('\nDict:')
my_dict = {'Валера': 2000, 'Лера': 2001}
print(my_dict)
print(my_dict.get('Лера'))
print(my_dict.get('Семен'))
my_dict['Ашан'] = 1961
my_dict['Python'] = 1991
del my_dict['Валера']
print(my_dict)

print('\nSet:')
set = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4}
print(set)
set.remove(4)
set.update({1, 2, 8, 9})
print(set)