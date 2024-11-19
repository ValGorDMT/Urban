immutable_var = (1, 2, [1, 2], 3, 4, 'a', 'b', 'c', True)
mutable_list = [1, 2, [1, 2], 3, 4, 'a', 'b', 'c', True]
print(f'Кортеж {immutable_var}\nСписок {mutable_list}')
# immutable_var[0] = 0 
# Ну незя так, кортеж неизменыемый объект, только если в нем нет изменяемого объекта к которому можно обратиться по типу списка, как представлено ниже:
immutable_var[2][1] = 55
mutable_list[0] = 0
print(f'Кортеж {immutable_var}\nСписок {mutable_list}')