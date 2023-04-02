"""
30.01.2022

Dasturlash asoslari

27-dars : КИРИЛЛ-LOTIN TELEGRAM BOT

Muallif: Shomansurov Oybek
"""
from transliterate import to_cyrillic, to_latin

import telebot

TOKEN='5137897469:AAGveoktizPap9xyGVbNmu83qj5wqp3bUxo'
bot = telebot.TeleBot(TOKEN, parse_mode=None)
   
@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalom alaykum, Xush kelibsiz!"
    javob+="\nMatn kiriting: "
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    if msg.isascii():
        javob=to_cyrillic(msg)
    else:
        javob=to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinity_polling()
# matn=input("Matn kiriting: ")

# if matn.isascii():
#       print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))