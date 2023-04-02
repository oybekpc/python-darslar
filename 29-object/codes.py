"""
02.02.2022

Dasturlash asoslari

29-dars : Obyektlar bilan ishlash

Muallif: Shomansurov Oybek
"""

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
    def set_bosqich(self,yangi_bosqich):
        """ Talabaning kursini yangilovchi metod """
        self.bosqich=yangi_bosqich
    
    def update_bosqich(self):
        """ Talabaning  bosqichini 1 taga ko'taradi"""
        self.bosqich+=1
    
    
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    def get_name(self):
        return self.ism
    
    def get_last(self):
        return self.familiya

talaba1 = Talaba("Alijon","Valiyev",2000)
talaba1.set_bosqich(3)
print(talaba1.get_info())    


class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
        
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]


matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)
# print(matematika.talabalar_soni)
# print(matematika.talabalar)

mat_talabalar=matematika.get_students()
print(mat_talabalar)