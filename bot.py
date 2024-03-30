import telebot
from telebot import types

user_sel = []
userdata = list(open('data.txt', 'r'))

bot = telebot.TeleBot('6995041657:AAH7KS37WX2mpGrURdejFsyDQ6G_EayUJUA')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Приветствуем Вас в сервисе онлайн мониторинга'
                                      ' <i>уязвимостей</i>. \nДля авторизации введите /reg', parse_mode='html', )


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
                                               "По команде /full будет предоставлена ссылка на полный список актуальных уязвимостей", parse_mode='html')

def keys(message):
    global components
    user_sel = message.text.strip().split()  # Разделение введенных номеров по пробелу
    keywords = []
    for num in user_sel:
        try:
            index = int(num) - 1  # Преобразование номера в индекс списка components
            if 0 <= index < len(components):  # Проверка допустимого диапазона индексов
                keywords.append(components[index].strip())  # Добавление выбранного компонента в keywords
        except ValueError:
            pass  # Пропустить неправильные вводы, которые не являются числами
    if keywords:
        bot.send_message(message.chat.id, text=f'Для отслеживания выбраны пункты {keywords}. Отслеживание начато')
        print(keywords)
        # Здесь должен быть ваш код для обработки ключевых слов и выполнения дальнейших действий
    else:
        bot.send_message(message.chat.id, text="Неверные номера компонентов. Повторите ввод.")



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
