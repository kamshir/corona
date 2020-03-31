import COVID19Py
import telebot

token = '1243293447:AAGs-5tDzJvxfbPwBgAaS_OkY9x_0ZhJ-6M'
bot = telebot.TeleBot(token)

telebot.apihelper.proxy = {'http':'http://russia-dd.proxy.digitalresistance.dog:443'}

covid19 = COVID19Py.COVID19()

latest = covid19.getLatest()

location = covid19.getLocationByCountryCode("RU")

@bot.message_handler(commands=['start'])

def start(message):
   send_mess = f"<b>Приветствую тебя, {message.from_user.first_name}!</b>\n Введите страну"
   bot.send_message(message.chat.id, send_mess, parse_mode='html')

bot.polling(none_stop=True)