"""
19.01.2022

Dasturlash asoslari

21-dars : Funksiya va Ro'yxat

Muallif : Shomansurov Oybek 
"""
# def harflar(matnlar):
#     for harf in range(len(matnlar)):
#         matnlar[harf]=matnlar[harf].title()
        
# ismlar=['ali','vali','hasan','husan']      
# harflar(ismlar)
# print(ismlar)

talabalar=['ali','vali','hasan','husan']      
def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

baholar = bahola(talabalar)
print(baholar)
print(talabalar)