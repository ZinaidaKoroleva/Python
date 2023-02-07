# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
import telebot

bot = telebot.TeleBot("5847616883:AAHLDM4BLbhCP289qmJaea-HLL1--Xj29HU")
flag = "Рациональные числа"
number1 = 0
number2 = 0
@bot.message_handler(commands=["start"])
def start(message):
    mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = telebot.types.KeyboardButton("Рациональные числа")
    key2 = telebot.types.KeyboardButton("Комплексные числа")
    mrk.add(key1)
    mrk.add(key2)
    bot.send_message(message.chat.id, "Выберите режим", reply_markup=mrk)
    bot.register_next_step_handler(message, number_type)

@bot.message_handler(content_types=["text"])
def number_type(message):
    global flag
    if message.text == "Комплексные числа":
        flag = "Комплексные числа"
    else:
        flag = "Рациональные числа"
    get_num1(message)

@bot.message_handler(content_types=["text"])
def get_num1(message):
    bot.send_message(message.chat.id, f"Введите первое число")
    bot.register_next_step_handler(message, change_num1)

@bot.message_handler(content_types=["text"])
def change_num1(message):
    global number1
    if flag == "Рациональные числа":
        number1 = int(message.text)
    else:
        number1 = complex(message.text)
    get_num2(message)

@bot.message_handler(content_types=["text"])
def get_num2(message):
    bot.send_message(message.chat.id, f"Введите второе число")
    bot.register_next_step_handler(message, change_num2)

@bot.message_handler(content_types=["text"])
def change_num2(message):
    global number2
    if flag == "Рациональные числа":
        number2 = int(message.text)
    else:
        number2 = complex(message.text)
    operation(message)

@bot.message_handler(content_types=["text"])
def operation(message):
    bot.send_message(message.chat.id, f"Введите знак")
    if flag == "Рациональные числа":
        bot.send_message(message.chat.id, f"Выбран режим {flag}, доступные знаки: +, -, *, /, //, %")
    else:
        bot.send_message(message.chat.id, f"Выбран режим {flag}, доступные знаки: +, -, *, /")
    bot.register_next_step_handler(message, calculations)

@bot.message_handler(content_types=["text"])
def calculations(message):
    if message.text == "+":
        res = number1+number2
    elif message.text == "-":
        res = number1-number2
    elif message.text == "*":
        res = number1*number2
    elif message.text == "/":
        res = number1/number2
    elif message.text == "//":
        res = number1//number2
    elif message.text == "%":
        res = number1 % number2
    bot.send_message(message.chat.id, f" {number1} {message.text} {number2} = {str(res)}")
    bot.send_message(message.chat.id, f"Новая операция: /start")

bot.infinity_polling()