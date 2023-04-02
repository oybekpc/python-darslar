"""
08.01.2022

Dasturlash asoslari

05-dars : Matn bilan ishlash (Strings)

Muallif : Shomansurov Oybek 
"""
viloyat="Farg'ona"
avto="Nexia 3"
matn="Men yangi 📱 oldim"
print(matn)

# Matnlarni qo'shish
ism="Ahad"
print("Mening ismim" + ism)
ism="Ahad"
familiya="Qayum"
print(ism +' ' + familiya)

ism="Oybek"
familiya="Shomansurov"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif)

fname="James"
Iname="Bond"
matn=f"Salom , mening ismim {Iname}.{fname} {Iname}"
print(matn)

tyil=2007
print(f"Siz {tyil}-yilda tug'ilgansiz")
print(f"Yoshingiz {2022-tyil} da")

#Maxsus belgilar
print("Hello \tWorld!")
print("Hello\nWorld!")

sim="Oybek"
familiya="Shomansurov"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())
print(ism_sharif.capitalize())
print(ism_sharif.strip())
print(ism_sharif.lstrip())
print(ism_sharif.rstrip())

ism=input("Ismingiz nima ? ")
print("Assalomu aleykum , " + ism.title())
print(f"Assalomu alaykum , {ism.title()}")








