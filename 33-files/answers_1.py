"""
06.02.2022

Dasturlash asoslari

33-dars : Fayllar bilan ishlash

Muallif: Shomansurov Oybek

Javoblar
"""

import pickle

with open('amaliyot/pi_million_digits.txt') as file:
    pi=file.read()
pi=pi.rstrip()
pi=pi.replace('\n','')
pi=pi.replace(' ','')

bdate='02062007'
print(bdate in pi)

pi=float(pi)

with open('amaliyot/pi_float.dat','wb') as file:
    pickle.dump(pi,file)