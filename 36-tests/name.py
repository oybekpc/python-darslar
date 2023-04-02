"""
14.02.2022

Dasturlash asoslari

36-dars : Funksiyani  Tekshirish 

Muallif : Shomansurov Oybek 
"""

def get_full_name(ism,familiya,otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()

