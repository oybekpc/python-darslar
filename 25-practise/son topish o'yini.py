"""
27.01.2022

Dasturlash asoslari

25-dars : "Son topish o'yini" 

Muallif : Shomansurov Oybek 
"""

from random import sample
sonlar=list(range(1,10))
y=sample(sonlar,k=2)
print("Keling o'ylagan sonni topish o'ynaymiz! ")
son=input("1 dan 10 gacha son o'yladim. Topa olasizmi? ")
print(son)
while son!=sample:
     if son==sample:
        print("Topdingiz! ")
     else:
        print("Xato")

