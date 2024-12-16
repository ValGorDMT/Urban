global_var = 'Я глобальная переменная'

def local_scope():
    global global_var
    local_var = "Я локальная переменная"
    global_var = 'Я гусь'
    print(f'Внутри функции {local_var}')
    print(f'Внутри функции {global_var}')

print(global_var)
local_scope()
print(global_var)



try:
    print(local_var)
except NameError as e:
    print(f'Ошибка: {e}')




def outer_func():
    outer_var = 'Я переменная внешней функции'

    def inner_func():
        inner_var = 'Я переменная внутреннкй функции'
        print( f'Внутри внутреннкй функции: {inner_var}')
        print( f'Внутри внутреннкй функции: {outer_var}')

    inner_func()
    print( f'Внутри внешней функции: {outer_var}')

    try:
        print(inner_var)
    except NameError as e:
        print(f'Ошибка: {e}')


outer_func()






def outer_func_with_nonlocal():
    outer_var = 'Я переменная внешней функции'

    def inner_func_with_nonlocal():
        nonlocal outer_var
        outer_var = 'Я измененная переменная внешней функции'
        print(f'Внутри внутренней функции {outer_var}')
    
    inner_func_with_nonlocal()
    print(f'Внутри внешней функции после изменения {outer_var}')

outer_func_with_nonlocal()