# a = [1,2,3,4,5,6]
# b = a.copy()
# a.clear()
# print(b)
# import datetime
# def random_int(num):
#     rand = datetime.datetime.now().microsecond/10**6
#     return int(num*rand)
# a = [1,2,3,4,5,6]
# random_int(5)
#
# for i in range(len(a) - 1, -1, -1):
#     j = random_int(i+1)
#     a[i],a[j] = a[j],a[i]
# print(a)

# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# import datetime
# def random_number(num):
#     rand = datetime.datetime.now().microsecond/10**6
#     return  int((num+1)*rand)
#
# n = int(input('Введите число: ' ))
# print(random_number(n))

# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# list_num = ["qwe", "FAS", "asd3"]
# find_num = int(input('Введите число: '))
# for i in range(len(list_num)):
#     if list_num[i] == find_num:
#         print('Число находится на позиции: ', i)
#         break
# else: print('Не найдено')
# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
#
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
#
# list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# find = "йцу"
# count = 0
# for i in range(len(list)):
#     if list[i] == find:
#         count += 1
#     if count == 2:
#         print(i)
#         break
# else:
#     print(-1)