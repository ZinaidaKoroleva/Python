# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# first_number = int(input('Введите первое число: '))
# second_number = int(input('Введите второе число: '))
# print('Первое число ', first_number, ' Второе число: ', second_number)
# if first_number==second_number**2 or second_number == first_number ** 2:
#     print ('да')
# else: print ('нет')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# a = int(input())
# max = a
# for i in range(4):
#     a = a = int(input())
#     if a > max:
#         max = a
# print(max)

# a = input()
# list_num = a.split()
# print(max(list_num))

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# number = int(input('Введите число: '))
# if number < 0:
#     number *= -1
# for i in  range(-number,number+1):
#     print(i, end=' ')

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# number = float(input('Введите число: '))
# if number % 1 == 0:
#     print("нет")

# else:
#     number = int (number * 10 % 10)
#     print(number)

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

number = float(input('Введите число: '))

if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and (number % 30 != 0):
    print('Кратно')
else:
    print('Не кратно')