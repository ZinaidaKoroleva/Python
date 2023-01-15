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

# number = int(input("Задайте натуральное число N: "))
# list = []
# len = number+1
# for i in range(2, len):
#     count = 0
#     for n in range(2, i+1):
#         if i % n == 0:
#             count += 1
#     if count == 1 and number % i == 0:
#         list.append(i)
#         number /= i
#         while number % i == 0:
#             list.append(i)
#             number /= i
#
# print(list)

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
# import random
# n = int(input("Задайте натуральную степень k: "))
# x = ['*x**', '*x', ' = 0']
# with open("polynomial.txt", "w") as file:
#     file.write("")
# for i in range(n, -1, -1):
#     factor = random.randint(0, 100)
#     if factor != 0 and i != 1 and i != 0:
#         with open("polynomial.txt", "a") as file:
#             file.write(str(factor))
#             file.write(str(x[0]))
#             file.write(str(i))
#             file.write(" + ")
#     if factor != 0 and i == 1:
#         with open("polynomial.txt", "a") as file:
#             file.write(str(factor))
#             file.write(str(x[1]))
#             file.write(" + ")
#     if i == 0 and factor != 0:
#         with open("polynomial.txt", "a") as file:
#             file.write(str(factor))
#
# with open("polynomial.txt", "a") as file:
#     file.write(str(x[2]))


# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def export_from_file(path):
    with open(path, "r") as file:
        polinom = file.read()
    return polinom

path1 = "file1.txt"
path2 = "file2.txt"

polynom1 = export_from_file(path1)
polynom2 = export_from_file(path2)
print(polynom1)
print(polynom2)
polynom1 = polynom1.split("+")
polynom2 = polynom2.split("+")
print(polynom1)
print(polynom2)

for indx,value in enumerate(polynom1):
    polynom1[indx] = list(map(int,(value.split("*x**"))))

for indx,value in enumerate(polynom2):
    polynom2[indx] = list(map(int,(value.split("*x**"))))

print(polynom1)
print(polynom1)

result_pol = polynom1+polynom2

polyn_dict = {}
for value in result_pol:
    if len(value)>1:
        if value[1] in polyn_dict.keys():
            polyn_dict[value[1]] +=value[0]
        else:
            polyn_dict[value[1]] = value[0]
    else:
        if 0 in polyn_dict.values():
            polyn_dict[0] +=value[0]
        else:
            polyn_dict[0] = value[0]

result_pol = dict(sorted(polyn_dict.items(), reverse=True))
finish_line = ""
for stepen,koeff in result_pol.items():
    if stepen > 1:
        finish_line +=f"{koeff}*x**{stepen}+"
    if stepen == 0:
        finish_line += f"{koeff}"

print(finish_line)