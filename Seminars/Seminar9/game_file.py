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