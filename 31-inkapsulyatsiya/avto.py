"""
05.02.2022

Dasturlash asoslari

31-dars : INKAPSULYATSIYA VA KLASSGA OID XUSUSIYAT VA METODLAR

Muallif: Shomansurov Oybek
"""

from uuid import uuid4
class Avto:
    """ Avtomobil klassi """
    __num_avto=0
    def __init__(self,make,model,rang ,yil,narh,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.__km=km
        self.__id=uuid4
        Avto.__num_avto+=1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
    def get_km(self):
        return self.__km()
    
    def get_id(self):
        return self.__id()
    
avto1=Avto("GM","Malibu","Qora",2020,40000,1000)
avto1=Avto("GM","Malibu","Qora",2020,40000,1000)
avto1=Avto("GM","Malibu","Qora",2020,40000,1000)