# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math
#
# d = input("Задайте точность: ")
# r = len(d)
# p = str(math.pi)
# print(f"Число Пи: {p}")
# print(p[:r])

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
# n = int(input("Задайте натуральное число N: "))
# for i in range(2,n+1):


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.

# import random
#
# a = [random.randint(0,4) for i in range(0,random.randint(7,11))]
# print(a)
# b = []
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         b.append(a[i])
# print(b)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
n = int(input("Задайте натуральную степень k: "))
x = ['*x**', '*x', ' = 0']
with open("polynomial.txt", "w") as file:
    file.write("")
for i in range(n, 0, -1):
    factor = random.randint(0, 100)
    if factor != 0 and i != 1:
        with open("polynomial.txt", "a") as file:
            file.write(str(factor))
            file.write(str(x[0]))
            file.write(str(i))
            file.write(" + ")
    if factor != 0 and i == 1:
        with open("polynomial.txt", "a") as file:
            file.write(str(factor))
            file.write(str(x[1]))
            file.write(" + ")
    if i == 0 and factor != 0:
        with open("polynomial.txt", "a") as file:
            file.write(str(factor))

with open("polynomial.txt", "a") as file:
    file.write(str(x[2]))


# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.