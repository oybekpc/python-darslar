"""
03.02.2022

Dasturlash asoslari

29-dars : Obyektlar bilan ishlash

Muallif: Shomansurov Oybek
Answers 2
"""

class Avtosalon:
    """Avtomobil xususiyatlari"""
    def __init__(self,nomi,manzili,avtomobil):
        self.nomi=nomi
        self.manzil=manzili
        self.avtomobil=avtomobil
        
    def update_avto(self):
        self.avtomobil += 1
    
    def get_avto(self):
        return self.avtomobil
    
    def get_info(self):
        return f"{self.nomi} {self.manzil} {self.avtomobil}"
        
        
avto1=Avtosalon("Uzmotors","toshkent","Gentra")
print(avto1.get_avto())
print(avto1.get_info())
        

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Avtosalon))

print(avto1.__dict__)

