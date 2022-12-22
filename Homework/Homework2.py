# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input('Введите число: ')
# sum = 0
# for i in number:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите число: '))
# list = []
# m = 1
# for i in range(1,number+1):
#     m *= i
#     list.append(m)
# print(list)

# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

# def create_list(a):
#     sum = 0
#     for i in range(1, a+1):
#         n = (1 + 1/i)**i
#         sum += n
#         print(round(n, 2), end='  ')
#     print('Сумма равна: ', round(sum, 2))
#
# create_list(4)

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.
import random

number = int(input('Введите число: '))
list = []

for i in range(0, number):          # задаем список
    list.append(random.randint(- number, number))
print(list)

pos = open("file.txt", "r")   # открываем файл с позициями
multiplication = 1
for i in pos:
    multiplication *= list[int(i)]    # находим произведение
print('Произведение: ', multiplication)

random.shuffle(list)   # алгоритм перемешивания.
print(list)