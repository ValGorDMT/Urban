print('Введите подрят три числа:')

number1 = input()
number2 = input()
number3 = input()

if number1 == number2 and number1 == number3:
    print('Все три числа равны между собой')
elif number1 == number2 or number1 == number3 or number2 == number3:
    print('Два числа между собой равны')
else:
    print('Нет равных между собой чисел')