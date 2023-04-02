"""
19.02.2022

Dasturlash asoslari

39-dars : PYTHON Tashqi Kutubxonasi

Muallif : Shomansurov Oybek 
"""

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from uzwords import words

# ikki so'z o'rtasida o'xshashlik foizini topish
print(fuzz.ratio("salom",'assalom'))
print(fuzz.ratio("salom","salim"))

# Matnlar orasidan 3 ta teng o'xshahslarini ajratib olish
text="салом"
matches=process.extract(text,words,limit=3)
print(matches)

# Matnlar orasida eng o'xshashini topish
text="талба"
match=process.extractOne(text,words)
print(match)
