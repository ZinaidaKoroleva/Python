# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
#
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#
# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#
#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )



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

def RLE_code(text):
    output_data = ''
    count = 0
    start_index = text[0]
    for end_index in text:

        if input_data_list[i+1]==input_data_list[i]:
            count+=1
        else:
            output_data.extend(list(input_data[count:input_data_list[i]]))
            count=1
input_data = "111112222334445"
code_data = RLE_code(input_data)
print(input_data)
print(code_data)