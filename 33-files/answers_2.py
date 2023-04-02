"""
06.02.2022

Dasturlash asoslari

33-dars : Fayllar bilan ishlash

Muallif: Shomansurov Oybek

Javoblar 2
"""

while True:
    book=input("Yaxshi ko'rgan kitobingizni kiriting (Dasturni"
               "to'xtatish uchun stop so'zini kiriting): ")
    if book=='stop':
        break
    with open('amaliyot/book.txt','a') as file:
        file.write(book+'\n')