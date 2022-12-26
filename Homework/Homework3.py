# 22.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# r_list = []
# list_len = random.randint(4,10)
# for i in range(list_len):
#     r_list.append(random.randint(0, 50))
# print(r_list)
# sum = 0
# for i in range(1, len(r_list), 2):
#     sum += r_list[i]
# print(sum)

# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def find_multi(list):
#     multi = 1
#     multi_list = []
#     if (len(list)%2) == 0:
#         for i in range(int(len(list)/2)):
#             multi = list[i]*list[(len(list)-1) - i]
#             multi_list.append(multi)
#     else:
#         for i in range((int(len(list)/2)+1)):
#             multi = list[i]*list[(len(list)-1) - i]
#             multi_list.append(multi)
#     return multi_list

# list1 = [2, 3, 4, 5, 6]
# list2 = [2, 3, 5, 6]
# print(list1, '=>', find_multi(list1))
# print(list2, '=>', find_multi(list2))

# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
#
# r_list = []
# list_len = random.randint(4, 10)
# for i in range(list_len):
#     r_list.append(random.randint(0, 200)+round(random.random(), 2))
# print(r_list)
#
# list = []
# for i in r_list:
#     if i % 1 != 0:
#         list.append(round(i % 1, 2))
# print(list)
# print(max(list))
# print(min(list))
# print(round(max(list) - min(list), 2))

# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
#
# num10 = int(input('Введите число: '))
# num2 = []
#
# while num10 > 0:
#     num2.append(num10 % 2)
#     num10 = num10//2
# num2.reverse()
# print("".join(map(str, num2)))

# 26.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def fib(n):
#     if n in (0,1):
#         return n
#     length = n + 1
#     fibs_pos = [0]*length
#     fibs_pos[1] = 1
#     for i in range (2, length):
#         fibs_pos[i] = (fibs_pos[i-1]+ fibs_pos[i-2])
#
#     fibs_neg = [0]*length
#     fibs_neg[1] = 1
#     for i in range(2, length):
#         fibs_neg[i] = fibs_neg[i-2] - fibs_neg[i-1]
#     fibs_neg.reverse()
#
#     return fibs_neg + fibs_pos[1:]
#
# f_n = int(input('Введите число: '))
# print(f"Fib: {fib(f_n)}")
