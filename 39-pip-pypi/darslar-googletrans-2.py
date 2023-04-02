"""
18.02.2022

Dasturlash asoslari

39-dars : PYTHON Tashqi Kutubxonasi

Muallif : Shomansurov Oybek 
"""

from googletrans import Translator
tarjimon = Translator()


msg="Tarjima uchun so'z kiriting (chiqib ketish uchun \"q\" deb yozing): "
while True:
    text=input(msg)
    if text =="q":
        break
    else:
        tarjima=tarjimon.trasnlate(text,src='uz',dest='en')
        print(tarjima.text)        
