import telebot
from telebot import types
import random
bot = telebot.TeleBot("5846731960:AAG8dvTrjIBVkR0DpCX8KTXV5r4M8EQX4e4")

candy = 221
step_max = 28
@bot.message_handler(commands = ['start'])#вызов функции по команде в списке
def start(message):
    bot.send_message(message.chat.id,f"/button")#отправка сообщения (кому отправляем, что отправляем(str))

@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)#создание клавиатуры
    but1 = types.KeyboardButton("Начать игру")#создание кнопок
    markup.add(but1)#добавление кнопок
    bot.send_message(message.chat.id,"Нажми на кнопку", reply_markup=markup)

def step_number(message):
    step = int(message.text)
    return step


@bot.message_handler(content_types=["text"])
def controller(message):
    if message.text == "Начать игру":
        global candy
        global step_max
        first_step = random.randint(1, 2)
        if first_step == 1:
            bot.send_message(message.chat.id,f"Первым ходит игрок")
        else:
            bot.send_message(message.chat.id,f"Первым ходит бот")
        while candy > 0:
            if first_step == 1:
                bot.send_message(message.chat.id, f"Игрок, введите количество конфет:")
                step = bot.register_next_step_handler(message, step_number)
                bot.send_message(message.chat.id, f"Пользователь взял {str(step)} конфет")
                if step <= 0 or step > 28:
                    bot.send_message(message.chat.id, f"Столько конфет нельзя брать!")
                else:
                    candy -= step
                    if candy < 0:
                        bot.send_message(message.chat.id, f"Столько конфет на столе нет!")
                        candy += step
                    else:
                        bot.send_message(message.chat.id, f"Конфет осталось {str(candy)}")
                        first_step = 2
            else:
                if candy <= step_max:
                    step = candy
                    print(f"Бот взял {step} конфет")
                    candy -= step
                    first_step = 1
                else:
                    step = random.randint(1, 28)
                    if step < candy:
                        print(f"Бот взял {step} конфет")
                        candy -= step
                        print(f"Конфет осталось {candy}")
                        first_step = 1
                    else:
                        step = candy
                        print(f"Бот взял {step} конфет")
                        candy -= step
                        first_step = 1
bot.infinity_polling()