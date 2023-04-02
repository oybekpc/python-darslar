"""
05.02.2022

Dasturlash asoslari

31-dars : INKAPSULYATSIYA VA KLASSGA OID XUSUSIYAT VA METODLAR

Muallif: Shomansurov Oybek

Javoblar 1
"""
from uuid import uuid4
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odamlar_soni=0
    def __init__(self,ism,familiya,yosh):
        self.ism=ism
        self.familiya=familiya
        self.__yosh=yosh
        self.__id=uuid4
        Shaxs.__odamlar_soni+=1
        
        
    @classmethod 
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni
    
    def get_ism():
        pass
    
    def get_familiya():
        pass   

shaxs1=Shaxs("Oybek","Shomansurov",15)
shaxs2=Shaxs("Shahzod","Rahiberdiyev",22)
print(Shaxs.get_odamlar_soni())