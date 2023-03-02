import os
from background import keep_alive  #импорт функции для поддержки работоспособности
import pip
import telebot
import time
import config

#Присваивание токена
bot = telebot.TeleBot(config.TOKEN)

# @bot.message_handler(content_types=['text'])
# def get_text_message(message):
#   bot.send_message(message.from_user.id, message.text)



# # echo-функция, которая отвечает на любое текстовое сообщение таким же текстом


#Функция повтора сообщений
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
  bot.send_message(message.chat.id, message.text)


#запускаем flask-сервер в отдельном потоке. Подробнее ниже...
keep_alive()

bot.polling(non_stop=True, interval=0)  #запуск бота 111111