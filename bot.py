import telebot
from telebot import types

user_sel = []
userdata = list(open('data.txt', 'r'))

bot = telebot.TeleBot('6995041657:AAH7KS37WX2mpGrURdejFsyDQ6G_EayUJUA')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Приветствуем Вас в сервисе онлайн мониторинга'
                                      ' <i>уязвимостей</i>. \nДля регистрации введите /reg', parse_mode='html', )


@bot.message_handler(commands=['reg'])
def handle_reg(message):
    bot.send_message(message.chat.id, 'Для продолжения необходимо авторизироваться')
    bot.send_message(message.chat.id, '<b>Логин:</b>', parse_mode='html')


name = None
password = None
login_check = 0
components = open('components.txt', 'r').readlines()


@bot.message_handler(content_types=['text'])
def user_login(message):
    global name
    name = message.text.strip()
    if login_check == 0:
        bot.send_message(message.chat.id, '<b>Пароль:</b>', parse_mode='html')
    bot.register_next_step_handler(message, user_password)
    if message.text == "Список компонентов":
        bot.send_message(message.chat.id, text="1. Operating systems\n2. DBMS\n3. Software protection tools\n4. Software and hardware protection\n5. Software for network hardware and software\n6. Network software\n7. Information Systems Application Software\n8. Software and hardware\n9. Automated control System software tool\n10. Firmware code\n\n<b>Введите номера необходимых пунктов через пробел</b>", parse_mode='html')



@bot.message_handler(content_types=['text'])
def keys(message):
    print(message)
    global components
    user_sel = list(message.text.strip())
    keywords = []
    list(map(int, user_sel))
    for i in range(len(components)):
        if str(i + 1) in user_sel:
            keywords.append(components[i])
    bot.send_message(message.chat.id, text=f'Для отслеживания выбраны пункты {keywords}. Отслеживание начато')
    print(keywords)
    from pars import parser
    reply = parser(keywords)
    bot.send_message(message.chat.id, text=reply)



def user_password(message):
    global password
    global login_check
    password = message.text.strip()
    for i in range(len(userdata)):
        if (name == userdata[i].split(":")[0]) and (password == userdata[i].replace("\n", "").split(":")[1]):
            bot.send_message(message.chat.id, '<b>Вы вошли</b>\nВам <i>доступен</i> список компонентов', parse_mode='html', reply_markup=markup)
            login_check = 1
            break
    if login_check == 0:
        bot.send_message(message.chat.id, '<b>Данные неверные</b>', parse_mode='html')
        handle_reg(message)


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Список компонентов")
markup.add(btn1)

bot.infinity_polling()
