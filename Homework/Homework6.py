# Формат: Объясняет преподаватель
#
# Задача: предложить улучшения кода для уже решённых задач:
# - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension

# **44. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# from math import sqrt
#
# distanse = lambda x1, y1, x2, y2: sqrt((x2-x1)**2 + (y2-y1)**2)
# print(distanse(3, 6, 2, 1)
# print(round(distanse(7, -5, 1, -1), 2))

# 45. Найти сумму чисел списка стоящих на нечетной позиции
# from random import randint
#
# list1 = [randint(0, 50) for i in range(randint(4, 10))]
# print(list1)
# sum_list = sum([v for i,v in enumerate(list1) if i % 2 == 1])
# print(sum_list)

# 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
#
# list1 = [2, 3, 4, 5, 6]
# list2 = [2, 3, 5, 6]
# list_multi1 = [list1[i] * list1[-i-1] for i in range(0, len(list1)//2 if len(list1) % 2 == 0 else len(list1)//2 + 1)]
# list_multi2 = [list2[i] * list2[-i-1] for i in range(0, len(list2)//2 if len(list2) % 2 == 0 else len(list2)//2 + 1)]
# print(list1, '=>',list_multi1)
# print(list2, '=>',list_multi2)

# 47.Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)

N = int(input("Введите длину: "))
n_list = [3**i if i % 2 == 0 else(-1)*3**i for i in range(0, N)]
print(n_list)
