"""
19.01.2022

Dasturlash asoslari

21-dars : Funksiya va Ro'yxat

Muallif : Shomansurov Oybek 
"""

def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
        
# talabalar=['Ali','Vali','Hasan','Husan']
# baholar=bahola(talabalar)
# print(baholar)
# print(talabalar)
# baholar=bahola(talabalar[:])
# print(talabalar)

talabalar=['Ali','Vali','Hasan','Husan']
baholar=bahola(talabalar[:])
print(talabalar)