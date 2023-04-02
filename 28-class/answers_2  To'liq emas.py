"""
01.02.2022

Dasturlash asoslari

28-dars : KLASSLAR

Muallif: Shomansurov Oybek

Javoblar 2
"""

class User:
    def __init__(self,name,username,email,age):
        self.ism=name
        self.fismi=username
        self.email=email
        self.yosh=age
        
    def get_name():
        pass
        
    def get_age():
        pass
        
    def get_email():
        pass
        
    def get_uname():
        pass
    
    def get_info(self):
        """To'liq ma'lumot chiqaradi """
        print(f"Foydalanuvchi:{self.username}, "
              "ismi: {self.name.title()}, email: "
              "{self.email,}, yoshi: {self.age}")
            
foydalanuvchi=User("Oybek", "Shomansurov01.u@zgmail.com",   )
print(foydalanuvchi.get_name())
print(foydalanuvchi.get_username())
print(foydalanuvchi.get_email())
print(foydalanuvchi.get_age())
print(foydalanuvchi.get_info())

