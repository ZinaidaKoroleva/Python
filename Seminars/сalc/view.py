
def view_result(a):
    print(f'Результат: {a}')

def get_value(a):
    if a == 1:
        return int(input('value = '))
    else:
        return complex(input('value = '))

def get_sign():
    return input('Введите знак: ')