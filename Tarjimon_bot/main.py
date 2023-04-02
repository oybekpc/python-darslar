"""
20.02.2022

Dasturlash asoslari

Mavzu: Telegram Bot   

Muallif : Shomansurov Oybek 
"""

from translate import translate
import telebot # pyTelegramBotAPI ning nomi

TOKEN="5169581772:AAGBrSXRpXQs9TSXqPUqxZFqgAc2ubAJAsw"
tarjimonbot = telebot.TeleBot(token=TOKEN)

@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar="Assalomu alaykum, tarjimmon botiga xush kelibsiz."
    xabar+='\nMatningizni yuboring.'
    tarjimonbot.reply_to(message,xabar)

@tarjimonbot.message_handler(func=lambda  msg:  msg.text is not None)
def tarjima(message):
    msg = message.text
    tarjimonbot.reply_to(message,translate(msg))


# botni ishga tushiramiz
tarjimonbot.polling()