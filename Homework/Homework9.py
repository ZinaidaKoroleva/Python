# На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

import telebot
import random

bot = telebot.TeleBot("5847616883:AAHLDM4BLbhCP289qmJaea-HLL1--Xj29HU")

flag = None
sweets = 221
max_sweet = 28
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Для начала игры введите /play")

@bot.message_handler(commands=["play"])
def play(message):
    global flag,sweets
    sweets = 221
    bot.send_message(message.chat.id, f"На столе лежит 221 конфета. Играют два игрока, делая ход друг после друга. "
                                      f"Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. "
                                      f"Все конфеты оппонента достаются сделавшему последний ход!")
    flag = random.choice(["user", "bot"])
    bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")
    if flag == "user":
        bot.send_message(message.chat.id,f"Первым ходите вы")  # отправка сообщения (кому отправляем, что отправляем(str))
    else:
        bot.send_message(message.chat.id,f"Первым ходит бот")# отправка сообщения (кому отправляем, что отправляем(str))
    controller(message)

def controller(message):
    global flag
    if sweets > 0:
        if flag == "user":
            bot.send_message(message.chat.id, f"Ваш ход. Введите кол-во конфет от 0 до {max_sweet}")
            bot.register_next_step_handler(message,user_input)
        else:
            bot_input(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Победил {flag}!")
        bot.send_message(message.chat.id, f"Для перезапуска введите /play")

def bot_input(message):
    global sweets, flag
    if sweets <= max_sweet:
        step_bot = sweets
    elif sweets % max_sweet == 0:
        step_bot = max_sweet - 1
        if step_bot == 0:
            step_bot = 1
    else:
        step_bot = sweets % max_sweet - 1
        if step_bot == 0:
            step_bot = 1
    sweets -= step_bot
    bot.send_message(message.chat.id, f"Бот взял {step_bot} конфет")
    bot.send_message(message.chat.id, f"Осталось {sweets} конфет")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

def user_input(message):
    global sweets, flag
    user_turn = int(message.text)
    sweets -= user_turn
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

bot.infinity_polling()

