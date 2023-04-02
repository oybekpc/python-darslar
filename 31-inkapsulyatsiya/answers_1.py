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
    def __init__(self,ism,familiya,yosh):
        self.ism=ism
        self.familiya=familiya
        self.__yosh=yosh
        self.__id=uuid4

    def get_id(self):
        return self.__id
    
    def get_yosh(self):
        return self.__yosh
    
    def add_yosh(self,yosh):
        """Shaxsning yoshiga yosh qo'shish"""
        if yosh>=0:
            self.__yosh+=yosh
        else:
            print("Yoshni kichraytirib bo'lmaydi")
            
    def get_info(self):
        info = f"Ismi:{self.ism} Familiyasi:{self.familiya}. "
        info += f"Yoshi {self.__yosh} da, ID:{self.__id}"
        return info 


shaxs1=Shaxs("Oybek","Shomansurov",15)
shaxs2=Shaxs("Shahzod","Rahiberdiyev",22)
