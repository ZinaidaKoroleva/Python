def input_error():
    return print("Ошибка ввода")
def success():
    return print("Данные записаны успешно!")

def menu():
    start = int(input('Меню(введите цифру): \n 1: Ввести новые данные \n 2: Показать весь справочник \n'
                 '3: Сортировка по имени или id \n 4: Вывод ФИО \n'))
    if start == 1 or start == 2 or start == 3 or start == 4:
        return start
    else:
        return input_error()

def get_date():
    # id, имя, фамилию, номер
    # телефона, комментрий
    new_number = ''
    id = input('Введите id: ')
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone_number = input('Введите номер телефона: ')
    comm = input('Введите комментарий: ')
    new_number = 'id: '+ id + ' Имя: '+name + ' Фамилия: '+ surname + ' Номер телефона: '+ phone_number + ' Комментарий: '+ comm
    return new_number

def menu_sort():
    number = int(input("Выберите пункт: \n 1: По имени \n2: По id \n"))
    return number