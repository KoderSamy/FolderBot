import telebot

TOKEN = '7075390755:AAGkHpZTdHIcnNsUkFc4d5gp6CgXhIOsgOE' # Ваш токен
bot = telebot.TeleBot(TOKEN)

# --- Информация о платформе ---
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton('/help'))
    keyboard.add(telebot.types.KeyboardButton('/info'))
    bot.send_message(message.chat.id, "Привет! Я чат-бот SculptVR. Чем я могу вам помочь?", reply_markup=keyboard)


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
                     "SculptVR - это интерактивная VR-платформа для обучения 3D-моделированию. Создавайте 3D-объекты прямо в виртуальном пространстве! \n"
                     "Возможности: \n"
                     "- Интерактивные уроки \n"
                     "- Многопользовательский режим \n"
                     "- Библиотека готовых моделей \n"
                     "- Кроссплатформенность \n"
                     "Стоимость: сто тыщ мильёнов \n"
                     "Поддерживаемые устройства: воздух \n"
                     "Подробнее: [Ссылка на сайт]")


# --- Обучение ---
@bot.message_handler(commands=['обучение', 'lessons'])
def lessons(message):
    bot.send_message(message.chat.id, "Как начать обучение? [инструкция] \n"
                                      "Доступные уроки: [список уроков/ссылка] \n"
                                      "Бесплатные уроки: [информация о бесплатных уроках/ссылка] \n"
                                      "Сертификат: [информация о сертификате/ссылка]")

# --- Техподдержка ---
@bot.message_handler(commands=['support', 'техподдержка'])
def support(message):
    bot.send_message(message.chat.id, "Опишите вашу проблему, и мы постараемся помочь. \n"
                                      "Также проверьте минимальные требования: [ссылка на требования]")
# --- Оплата и подписка ---
@bot.message_handler(commands=['оплата', 'подписка', 'payment', 'subscription'])
def payment(message):
    bot.send_message(message.chat.id, "Оплата подписки: [ссылка на страницу оплаты] \n"
                                      "Виды подписки: [описание видов подписки] \n"
                                      "Отмена подписки: [инструкция]")

# --- Сообщество ---
@bot.message_handler(commands=['сообщество', 'community'])
def community(message):
    bot.send_message(message.chat.id, "Присоединиться к сообществу: [ссылка на сообщество] \n"
                                      "Работы пользователей: [ссылка на галерею]")

# --- Отзывы и предложения ---
@bot.message_handler(commands=['отзыв', 'предложение', 'feedback', 'suggestion'])
def feedback(message):
    bot.send_message(message.chat.id, "Оставить отзыв: [ссылка на форму] \n"
                                      "Написать отзыв здесь:")


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
                     "Доступные команды:\n"
                     "/info - информация о SculptVR\n"
                     "/обучение - информация об обучении\n"
                     "/техподдержка - обратиться в техподдержку\n"
                     "/оплата - информация об оплате и подписке\n"
                     "/сообщество - присоединиться к сообществу\n"
                     "/отзыв - оставить отзыв или предложение" )

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "Извините, я не понимаю ваш запрос. Используйте /help.")


bot.infinity_polling()