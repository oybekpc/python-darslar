"""
03.02.2022

Dasturlash asoslari

30-dars : Vorislik va Polimorfizm

Muallif: Shomansurov Oybek
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil

    def get_info(self):
         """Shaxs haqida ma'lumot """
         info=f"{self.ism} {self.familiya}. "
         info+=f"Passport: {self.passport}, {self.tyil}"
         return info
    def get_age(self,yil):
         """Shaxsning yoshini qaytaruvchi metod"""
         return yil-self.tyil
     
inson=Shaxs("Hasan","Alimov","FB001122",1995)
print(f"{inson.get_info()} . {inson.get_age(2022)} yoshda")

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam=idraqam
        self.bosqich = 1

    def get_id(self):
            """Talabaning ID raqami"""
            return self.idraqam
        
    def get_bosqich(self):
            """Talabaning o'qish bosqichi"""
            return self.bosqich
    
    def get_info(self):
         """Talaba haqida ma'lumot """
         info=f"{self.ism} {self.familiya}. "
         info+=f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
         return info










