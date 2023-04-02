"""
18.02.2022

Dasturlash asoslari

39-dars : PYTHON Tashqi Kutubxonasi

Muallif : Shomansurov Oybek 
"""

# pip install googletrans==3.1.0a0
from googletrans import Translator
tarjimon=Translator()

matn_uz="Python - dunyodagi eng mashhur dasturlash tili"
tarjima=tarjimon.tarnslate(matn_uz)
# Original matn
print(tarjima.origin)
# Tarjima
print(tarjima.text)
# Original matn tili
print(tarjima.src)

# Boshqa tilga tarjima qilish uchun dest parametridan foydalanamiz
tarjima_ru=tarjimon.translate(matn_uz,dest='ru')
print(tarjima_ru.text)

# Ingliz tilidan tarjima
matn_en="Tashkent is the capital of Uzbekistan"
tarjima_uz=tarjimon.translate(matn_en,dest='uz')
print(tarjima_uz.text)
