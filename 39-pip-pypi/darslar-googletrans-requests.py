"""
18.02.2022

Dasturlash asoslari

39-dars : PYTHON Tashqi Kutubxonasi

Muallif : Shomansurov Oybek 
"""

import requests 
import googletrans

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()['slip']['advice']
print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice,dest='uz')
print(tarjima.text)
