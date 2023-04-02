"""
01.02.2022

Dasturlash asoslari

28-dars : KLASSLAR

Muallif: Shomansurov Oybek
"""

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil        
        
    def get_name(self):
        return self.ism
        
    def get_age(self,yil):
        return yil - self.tyil
    
    def get_lastname(self):
        return self.familiya
                
    def tanishtir(self):
        return(f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil} ")

talaba1=Talaba("Olim","Olimov",2000)
talaba2=Talaba("Hasan","Husanov",2004)
talaba3=Talaba("Oybek","Shomansurov",2007)
talaba4=Talaba("Hasan","Akbarov",2004) 
talaba4.tanishtir()

class User:
    def __int__(self,name,username,email):
        self.name=name
        self.uname=username
        self.mail=email
        def describe():
            pass
        def get_email():
            pass