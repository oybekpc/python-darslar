"""
09.01.2022

Dasturlash asoslari

07-dars : Lists (Ro'yxatlar)

Muallif : Shomansurov Oybek 
"""
ismlar=['Shahzod','Javohir','Sunnat']
print(ismlar[0] + " aka zukkolar va landavurlar kitobini o'qib bo'ldizmi? ")
print("Cambridge qachondan boshlanadigan bo'ldi " + ismlar[2] + " aka")
print("Assalom alaykum " + ismlar[1] + " aka ishlariz yaxshimi . Kitoblar uchun katta rahmat.")

sonlar=[16,-89,53,-135,90,-24.57]
sonlar[3]=678
sonlar[-2]=446
sonlar[2]=sonlar[2]+34
print(sonlar)

t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim\n")

friends=[]
friends.append("Shahzod")
friends.append("Javohir")
friends.append("Sunnat")
friends.append("Saidazm")
print(friends)

friends.remove("Saidazm")
print(friends)

friends.insert(2,"Jahongir")
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)