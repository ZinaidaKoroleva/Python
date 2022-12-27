# 27. Задайте строку из набора чисел. Напишите программу,которая покажет большее и меньшее число:
# В качестве символа разделителя используйте пробел.

# nums = (input('Введите числа через пробел: ')).split()
# max = int(nums[0])
# min = int(nums[0])
# for i in range(len(nums)):
#     if int(nums[i]) > max:
#         max = int(nums[i])
#     if int(nums[i]) < min:
#         min = int(nums[i])

# print(f"min = {min} max = {max}")

# 28. Найдите корни квадратного уравнения Ах^2 + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python.
import math
# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))
#
# dis = math.pow(b,2) - 4*a*c
# print(dis)
# if a!=0:
#     if dis > 0:
#         x1 = (-b+dis**0.5)/ (2*a)
#         x2 = (-b-dis**0.5)/ (2*a)
#         x1 = (-b+math.sqrt(dis))/ (2*a)
#         x2 = (-b-math.sqrt(dis))/ (2*a)
#         print(f" x1 = {x1}, x2 = {x2}")
#     elif dis = 0:
#         x = -b/(2*a)
#         print(f"x = {x}")
#     else:
#          print("Корней нет")
# else:
#     x = -c / b

# 29. Задайте два числа. Напишите программу,которая найдет НОК этих двух чисел.

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# if a % b == 0:
#     print(f"НОК = {a}")
# if b % a == 0:
#     print(f"НОК = {b}")
# for i in range(max(a,b), a*b + 1, max(a,b)):
#     if i % a == 0 and i % b == 0:
#         print(f"НОК = {i}")
#         break
