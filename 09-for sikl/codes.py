"""
11.01.2022

Dasturlash asoslari

09-dars : For tsikli

Muallif : Shomansurov Oybek 
"""
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)
    
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
print("Hurmat bilan, Palonchiyevlar oilasi\n")

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)
    print(mehmonlar) 

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")

sonlar = list(range(11)) 
sonlar_kvadrati =[] 
for son in sonlar: 
    sonlar_kvadrati.append(son**2) 
print(sonlar)
print(sonlar_kvadrati)

dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)









