# list = [(i,i) for i in range(1, 21) if i % 2 == 0]
# print(list)

# def f(x):
#     return x**3
#
# list = [(i, f(i)) for i in range (1,21) if i % 2 == 0 ]
# print(list)
#
# def select(f, col):
#     return  [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = select(int, data)
# res = where(lambda  x: not x %2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# Начало семинара

# a = []
# for i in range(1,9):
#     a.append(i)
# print(a)

# a = [i*i for i in range(1,9)]
# print(a)

#enumerate

# a = [1, 4, 9, 16, 25, 36, 49, 64]
# for indx,value in enumerate(a):
#     print(indx,value)

# zip
# num = [1,2,3,4,5,6]
# months = ["июнь", "июль","июль2","июль3","июль4","июль5",]
# a = list(zip(num,months))
# print(a)

#lambda
# def summ(a,b):
#     return  a+b
# print(summ(3,5))

# summ = lambda a, b: a+b if a > 5 else 0
# print(summ(2,5))

# map
# a = [i for i in range(12)]
# print(a)
# a = list(map(lambda x: x+10 if x>6 else x + 0, a))
# print(a)

#filter
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# def chek_num(x):
#     if x % 2 == 0:
#         return  True
# a_chet = list(filter(chek_num,a))
# print((a_chet))

#35) Напишите программу для поиска пересечения двух заданных массивов с помощью Lambda.
# [1 , 2, 3, 5, 6, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
#
# num1 = [1, 2, 3, 5, 6, 7, 8, 9, 10]
# num2 = [1, 2, 4, 8, 9]
# res = list(filter((lambda x: x in num1), num2))
# print(res)

# 36) Сделать с помощью filter, lambda
# Напишите программу, удаляюшую из текста все слова, содержащие "абв".
# Вывести все пробелы и их индексы из предыдущей строки.

# str = 'фыыо лыбш, уальуц а абв фбвб фыфыкфф цабвыц'
# lst = str.split()
# list2 = ' '.join(filter(lambda x: 'абв' not in x, lst))
# print(list2)
#
# for i, sum in enumerate(str):
#     if sum == ' ':
#         print(i, sum)

# 37) Имеется упорядоченный список:
# A = [[1,2,3], [4,5,6], [7,8,9]]
# Перебрать все элементы этого списка с помощью функций enumerate и элементы,
# стоящие на главной диагонали (имеющие равные индексы), превратить в нули.

# a = [[1,2,3], [4,5,6], [7,8,9]]
#
# for i,v in enumerate(a):
#     v[i] = 0
# print(a)

# 38) Имеется список id сотрудников из 10 элементов, каждый id - случаное число от 1 до 100.
# Имеется список имент сотрудников из 10 элементов. Сопоставьте каждому имени сотрудника его id
# и выведите получившийся список. Выведите имена сотрудников, получивших нечетное id.
# import random
# id = [random.randint(1,100) for _ in range(5)]
# names = ['ivanov','petrov','sidorov', 'kuznecov', 'potapov']
# lst = list(zip(id,names))
# print(lst)
#
# lst_odd = [elem[1] for elem in lst if elem[0] % 2 !=0]
# print(lst_odd)