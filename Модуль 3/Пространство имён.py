calls = 0


def count_calls():
    global calls
    calls += 1

def string_info(string_in):
    count_calls()
    return((len(string_in), string_in.upper(), string_in.lower()))

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        exet = False
        if string.lower() == list_to_search[i].lower():
            exet = True
            break
    return(exet)

print(string_info('Интересное — на почту!'))
print(string_info('Программирование'))
print(is_contains("ПрограММировАние", ['Программирование', 'Менеджмент', 'Образование']))
print(is_contains("Программирование", ['Дизайн', 'Разработка', 'Маркетинг']))
print(calls)


# Выход такой:
# (22, 'ИНТЕРЕСНОЕ — НА ПОЧТУ!', 'интересное — на почту!')
# (16, 'ПРОГРАММИРОВАНИЕ', 'программирование')
# True
# False
# 4
