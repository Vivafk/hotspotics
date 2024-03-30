import telebot
from telebot import types


user_sel=[]
userdata = list(open('data.txt', 'r'))
print(userdata)
print(userdata[0].split(":")[0], userdata[0].replace("\n", "").split(":")[1])
print(userdata[1].split(":")[0], userdata[1].replace("\n", "").split(":")[1])


bot = telebot.TeleBot('6995041657:AAH7KS37WX2mpGrURdejFsyDQ6G_EayUJUA')

@bot.message_handler(commands=['start'])
def handle_start(message):

    bot.send_message(message.chat.id, 'Приветствуем Вас в сервисе онлайн мониторинга'
                                      ' <i>уязвимостей</i>. \nДля регистрации введите /reg' , parse_mode='html', )
@bot.message_handler(commands=['reg'])
def handle_reg(message):
    bot.send_message(message.chat.id, 'Для продолжения необходимо авторизироваться')
    bot.send_message(message.chat.id, '<b>Логин:</b>', parse_mode='html')

# @bot.message_handler(commands=['full'])
# def handle_full(message):
#     bot.send_message(message.chat.id, 'По данной ссылке можете скачать файл.'
#                                       '\nhttps://bdu.fstec.ru/files/documents/vullist.xlsx',parse_mode='html')


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
                                               "1.Операционные системы\n"
                                               "2.СУБД\n"
                                               "3.Программные средства защиты\n"
                                               "4.ПО программно-аппаратных средств защиты\n"
                                               "5.ПО сетевого программно-аппаратного средства\n"
                                               "6.Сетевое программное обеспечение\n"
                                               "7.Прикладное ПО информационных систем\n"
                                               "8.ПО программно-аппаратного средства\n"
                                               "9.Программное средство АСУ ТП\n"
                                               "10.Микропрограммный код\n"
                                               "Для выбора компонента напишите его номер .\n"
                                               "Вы также можете создать отдельный проект и добавить в него уязвимости.\n"
                                               "По команде /full будет предоставлена ссылка на полный список актуальных уязвимостей")
    if (message.text == "1"): user_sel.append(1)
    if (message.text == "2"): user_sel.append(2)
    if (message.text == "3"): user_sel.append(3)
    if (message.text == "4"): user_sel.append(4)
    if (message.text == "5"): user_sel.append(5)
    if (message.text == "6"): user_sel.append(6)
    if (message.text == "7"): user_sel.append(7)
    if (message.text == "8"): user_sel.append(8)
    if (message.text == "9"): user_sel.append(9)
    if (message.text == "10"): user_sel.append(10)
    o = open('components.txt', 'r').readlines()
    keywords = []
    list(map(int, user_sel))
    for i in range(len(o)):
        if str(i+1) in user_sel:
            keywords.append(o[i])
    print(keywords)


def user_password(message):
    global password
    global login_check
    password = message.text.strip()
    for i in range(len(userdata)):
        if (name == userdata[i].split(":")[0]) and (password == userdata[i].replace("\n", "").split(":")[1]):
            bot.send_message(message.chat.id,'<b>Вы вошли</b>\nВам <i>доступен</i> список компонентов',
                             parse_mode='html',reply_markup=markup )
            login_check = 1
            break
    if login_check == 0:
        bot.send_message(message.chat.id, '<b>Данные неверные</b>', parse_mode='html')
        handle_reg(message)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Список компонентов")
markup.add(btn1)


bot.infinity_polling()