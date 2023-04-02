"""
08.01.2022

Dasturlash asoslari

05-dars : Matn bilan ishlash (Strings)

Muallif : Shomansurov Oybek 
"""
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f"{kocha} ko'chasi , {mahalla} mahallasi , {tuman} tumani , {viloyat} viloyati .")

print("Iltimos quyidagi ma'lumotlarni kiring :")
kocha=input("Qaysi ko'chada yashaysiz ? ")
mahalla=input("Qaysi mahallada yashaysiz ? ")
tuman=input("Qaysi tumanda yashaysiz ? ")
viloyat=input("Qaysi viloyatda yashaysiz ? ")
print(f"{kocha} ko'chasi ,\n{mahalla} mahallasi ,\n{tuman} tumani ,\n{viloyat} viloyati .")

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)
manzil = f"{kocha.capitalize()} ko'chasi, {mahalla.title()} mahallasi, {tuman.lower()} tumani, {viloyat.upper()} viloyati"
print(manzil)










