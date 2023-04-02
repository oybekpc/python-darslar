"""
11.01.2022

Dasturlash asoslari

09-dars : For tsikli

Muallif : Shomansurov Oybek 
"""
ismlar=['Oybek','Ozodbek','Muhammadjon','Shahzod','Javohir']
for ism in ismlar:
    print(f"Assalom alaykum, {ism} . Ahvollaringiz yaxshimi")
print(f"Kod {len(ismlar)} marta takrorlandi.")

toq_sonlar=list(range(11,100,2))
for sonlar in toq_sonlar:
    print(f"{sonlar} ning kubi {sonlar**3}")

kinolar=[]
print("5 ta eng sevimli kinoingizn kiriting.")
for n in range(5):
    kinolar.append(input(f"{n+1}-sevimli kinoingiz: "))
print(kinolar)
    
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)




 