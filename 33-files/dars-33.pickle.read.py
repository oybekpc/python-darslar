"""
06.02.2022

Dasturlash asoslari

33-dars : Fayllar bilan ishlash

Muallif: Shomansurov Oybek
"""

import pickle

with open('info','rb') as file:
    talaba1=pickle.load(file)
    talaba2=pickle.load(file)

print(talaba1)
print(talaba2)