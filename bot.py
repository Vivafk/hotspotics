import telebot

userdata = list(open('data.txt', 'r'))
print(userdata)
print(userdata[0].split(":")[0], userdata[0].replace("\n", "").split(":")[1])
print(userdata[1].split(":")[0], userdata[1].replace("\n", "").split(":")[1])

bot = telebot.TeleBot('6995041657:AAH7KS37WX2mpGrURdejFsyDQ6G_EayUJUA')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Hello! To continue working, you need to log in')
    bot.send_message(message.chat.id, '<b>Login:</b>', parse_mode='html')


name = None
password = None
login_check = 0


@bot.message_handler(content_types=['text'])
def user_login(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, '<b>Password:</b>', parse_mode='html')
    bot.register_next_step_handler(message, user_password)


def user_password(message):
    global password
    global login_check
    password = message.text.strip()
    for i in range(len(userdata)):
        if (name == userdata[i].split(":")[0]) and (password == userdata[i].replace("\n", "").split(":")[1]):
            bot.send_message(message.chat.id,'<b>МЫ ВОШЛИ</b>', parse_mode='html' )
            login_check = 1
            break
    if login_check == 0:
        bot.send_message(message.chat.id, '<b>Данные неверные</b>', parse_mode='html')

bot.infinity_polling()