"""
20.02.2022

Dasturlash asoslari

Mavzu: Telegram Bot   

Muallif : Shomansurov Oybek 
"""

from googletrans import Translator


def translate(matn):
    translator=Translator()
    # matn tilini aniqlaymzi:
    til=translator.detect(matn).lang
    if til=='en': # agar matn ingliz tilida bo'lsa...
        return translator.translate(matn,dest='uz').text
    else:
        return translator.translate(matn,dest='en').text

