def input_error():
    return print("Ошибка ввода.")
def repit_error():
    return print("Такая запись уже существует.")
def menu():
    start = int(input('Меню(введите цифру): \n 1: Добавить нового студента \n 2: Добавить предмет \n'
                      ' 3: Добавить оценку ученику по предмету \n 4: Показать список учеников \n '
                      '5: Показать лист оценок конкретного ученика \n 6:Выход \n'))

    if start == 1 or start == 2 or start == 3 or start == 4 or start == 5 or start == 6:
        return start
    else:
        return input_error()
def get_student():
    return input('Введите имя и фамилию: ')
def get_schoolwork():
    return input('Введите предмет: ')
def get_mark():
    return input('Введите оценку: ')


