# a = {4:"ffdsf", 2:"dsd", 3:"d"}
# r = sorted(a)
# print(r)
# 41) Наришите программу, которая сортирует элементы массива по возрастанию последней цифры десятичной записи чисел.
# Входные данные:
# 6
# 219 234 890 81 73 96
# Первая строка содержит размер массива N. Во второй строке черезх пробел задаются N чисел - элементы массива. Гарантируетс, что 0<N<100.
#
# Выходные данные
# 890 81 73 234 96 219
# Программа должна вывести в одной строке элементы массива, отсортированного в порядке возрастания
# посденей цифры в десятичной записи чисел, разделив их пробелами. Числа, у которых последняя цифра одинаковая,
# должны быть выведены в том же порядке, в котором они стояли в исходной последовательности.
# a = [219, 234, 890, 66, 81, 73, 96]
# r = sorted(a, key=lambda x: x % 10)
# print(r)

# 42)Напишите программу, которая сортирует натуральные числа в массиве по убыванию суммы цифр.
#
# a = [9, 21, 32, 55, 81, 11]
#
# def num(x:int):
#     sum = 0
#     while x > 0:
#         sum += x%10
#         x //= 10
#     return sum
#
# r = sorted(a, key=num, reverse=True)
# print(a)
# print(r)

# 43) Напишите программу,
# Решение 1:
# def merge(keys, values):
#     res = []
#     for i in range(len(keys)):
#         res.append((keys[i], values[i]))
#     return res
#
# a = [3, 1, 2, 3, 4, 6]
# print(a)
# dict = list(enumerate(a))
# odd = list(filter(lambda v: not v[1]%2==0,dict))
# even = list(filter(lambda v: v[1]%2==0,dict))
# keys = [v[0] for v in odd]
# values = sorted([v[1] for v in odd])
# odd = merge(keys, values)
# keys1 = [v[0] for v in even]
# values1 = sorted([v[1] for v in even], reverse=True)
# even = merge(keys1, values1)
# res = odd+even
# res = sorted(res, key=lambda x: x[0])
# result = [i[1] for i in res]
# print(result)
# Решение 2:

# a = [3, 1, 2, 3, 4, 6]
# print(a)
# h = [1 if i % 2 == 0 else 0 for i in a]
# print(h)
# even = [i for i in a if i % 2 == 0]
# odd = [i for i in a if i % 2 == 1]
# even.sort(reverse=True)
# odd.sort()
# print(even)
# print(odd)
#
# for index,value in enumerate(h):
#     if value == 1:
#         h[index] = even.pop(0)
#     else:
#         h[index] = odd.pop(0)
# print(h)
#
