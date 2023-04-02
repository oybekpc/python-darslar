"""
05.02.2022

Dasturlash asoslari

31-dars : INKAPSULYATSIYA VA KLASSGA OID XUSUSIYAT VA METODLAR

Muallif: Shomansurov Oybek
"""

from uuid import uuid4
class Avto:
    """ Avtomobil klassi """
    def __init__(self,make,model,rang ,yil,narh,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.__km=km
        self.__id=uuid4
        
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id()
    
    def add_km(self,km):
        "Mashinaning km ga yana km qo'shish"
        if km>=0:
            self.__km+=km
        else:
            print("Mashinani km ni kamaytirib bo'lmaydi")
    
avto1=Avto("GM","Malibu","Qora",2020,40000,1000)
