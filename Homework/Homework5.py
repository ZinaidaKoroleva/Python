# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале.
# Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой.
# В конце вывести игрока, который победил
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )
import random
print("----Игра с конфетами----")
print('Условия игры: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.\n Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \n Все конфеты оппонента достаются сделавшему последний ход')
mode = int(input('Выберите режим(введите цифру): \n 1: Игрок против игрока  \n 2: Игрок против бота \n '))
candy = 221
step_max = 28
if mode == 1:
    player = random.randint(1, 2)
    print(f"Первым ходит игрок {player}")
    while candy > 0:
        step = int(input(f"Игрок {player}, введите количество конфет:"))
        if step <= 0 or step > 28:
            print(f"Столько конфет нельзя брать!")
        else:
            candy -= step
            if candy < 0:
                print(f"Столько конфет на столе нет!")
                candy+=step
            else:
                print(f"На столе осталось {candy} конфет")
                if player == 1:
                    player = 2
                else:
                    player = 1
    if player == 1:
        player = 2
    else:
        player = 1

    print(f"Победил игрок {player} ")
else:
    first_step = random.randint(1, 2)
    if first_step==1:
        print(f"Первым ходит игрок")
    else:
        print(f"Первым ходит бот")
    while candy > 0:
        if first_step==1:
            step = int(input("Игрок, введите количество конфет:"))
            if step <= 0 or step > 28:
                print(f"Столько конфет нельзя брать!")
            else:
                candy -= step
                if candy < 0:
                    print(f"Столько конфет на столе нет!")
                    candy += step
                else:
                    print(f"Конфет осталось {candy}")
                    first_step = 2
        else:
            if candy <= step_max:
                step = candy
                print(f"Бот взял {step} конфет")
                candy -= step
                first_step = 1
            else:
                step = random.randint(1,28)
                if step<candy:
                    print(f"Бот взял {step} конфет")
                    candy -= step
                    print(f"Конфет осталось {candy}")
                    first_step = 1
                else:
                    step=candy
                    print(f"Бот взял {step} конфет")
                    candy -= step
                    first_step = 1

    if first_step == 1:
        print(f"Победил бот!")
    else:
        print(f"Победил игрок!")

# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.
#
# def RLE_code(data):
#     output_data = ''
#     count = 0
#     start_index = data[0]
#     for end_index in data:
#         if end_index!=start_index:
#             output_data+=f"{count}{start_index}"
#             start_index=end_index
#             count=1
#         else:
#             count+=1
#     else:
#         output_data+=f"{count}{start_index}"
#     return output_data
#
# def RLE_decode(data):
#     decode_text = ""
#     digit = True
#     count = 0
#     for i in data:
#         if digit:
#             count = int(i)
#             digit= False
#         else:
#             decode_text+=count*i
#             digit = True
#     return decode_text
#
# input_data = "111112222334445"
# print(f"Исходные данные: {input_data}")
# code_data = RLE_code(input_data)
# print(f"Сжатые данные: {code_data}")
# decode_data = RLE_decode(code_data)
# print(f"Раскодировка: {decode_data}")
# input_text = "AAAAAAFDDCCCCCCCAEEEEEEEEE"
# print(f"Исходный текст: {input_text}")
# code_text = RLE_code(input_text)
# print(f"Сжатый текст: {code_text}")
# decode_text=RLE_decode(code_text)
# print(f"Раскодировка: {decode_text}")