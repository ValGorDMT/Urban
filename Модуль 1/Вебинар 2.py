import random

num = random.randint(1, 100)
print(num)

points = 5
errorPoints = 0

while points > errorPoints:
    answer = int(input('Введите число, которое загадал комрьютер: '))
    if answer == num:
        print("Верно!")
        break

    elif answer > num:
        print('Мое число меньше')
        errorPoints += 1
    elif answer < num:
        print('Мое число больше')
        errorPoints += 1