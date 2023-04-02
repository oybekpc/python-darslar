"""
02.02.2022

Dasturlash asoslari

29-dars : Obyektlar bilan ishlash

Muallif: Shomansurov Oybek
"""

class Avto:
    """Avtomobil xususiyatlari"""
    def __init__(self,model,rang,korobka,narx):
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narx=narx
        self.kilometr=0
        
    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_narx(self):
        return self.narx
    
    def get_info(self):
        return f"Modeli: {self.model}, Rangi: {self.rang}, Korobka:{self.korobka}, Narx:{self.narx} "

    def update_km(self,km):
        self.kilometr+=1
        
avto1=Avto("Malibu","Qora","Korobka",27000)
print(avto1.get_info())
print(avto1.get_model())