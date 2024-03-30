import telebot
from telebot import types

userdata = list(open('data.txt', 'r'))
print(userdata)
print(userdata[0].split(":")[0], userdata[0].replace("\n", "").split(":")[1])
print(userdata[1].split(":")[0], userdata[1].replace("\n", "").split(":")[1])

bot = telebot.TeleBot('6995041657:AAH7KS37WX2mpGrURdejFsyDQ6G_EayUJUA')

@bot.message_handler(commands=['start'])
def handle_start(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("Список компонентов")
    # markup.add(btn1)
    bot.send_message(message.chat.id, 'Приветствуем Вас в сервисе онлайн мониторинга'
                                      ' <i>уязвимостей</i>. \nДля регистрации введите /reg' , parse_mode='html', )
@bot.message_handler(commands=['reg'])
def handle_reg(message):
    bot.send_message(message.chat.id, 'Для продолжения необходимо авторизироваться')
    bot.send_message(message.chat.id, '<b>Логин:</b>', parse_mode='html')

name = None
password = None
login_check = 0

@bot.message_handler(content_types=['text'])
def user_login(message):
    global name
    name = message.text.strip()
    if login_check == 0:
        bot.send_message(message.chat.id, '<b>Пароль:</b>', parse_mode='html')
    bot.register_next_step_handler(message, user_password)
    if (message.text == "Список компонентов"):
        bot.send_message(message.chat.id, text="Вот актуальный список компонентов:\n"
                                               "Операционные системы\n"
                                               "СУБД\n"
                                               "Программные средства защиты\n"
                                               "ПО программно-аппаратных средств защиты\n"
                                               "ПО сетевого программно-аппаратного средства\n"
                                               "Сетевое программное обеспечение\n"
                                               "Прикладное ПО информационных систем\n"
                                               "ПО программно-аппаратного средства\n"
                                               "Программное средство АСУ ТП\n"
                                               "Микропрограммный код\n"
                                               "Для выбора компонента напишите / и название компонента как в данном сообщении.")


def user_password(message):
    global password
    global login_check
    password = message.text.strip()
    for i in range(len(userdata)):
        if (name == userdata[i].split(":")[0]) and (password == userdata[i].replace("\n", "").split(":")[1]):
            bot.send_message(message.chat.id,'<b>Вы вошли</b>\nВам <i>доступен</i> список компонентов', parse_mode='html',reply_markup=markup )
            login_check = 1
            break
    if login_check == 0:
        bot.send_message(message.chat.id, '<b>Данные неверные</b>', parse_mode='html')
        handle_reg(message)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Список компонентов")
markup.add(btn1)



bot.infinity_polling()