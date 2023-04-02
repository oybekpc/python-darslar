"""
12.01.2022

Dasturlash asoslari

10-dars : if-else 

Muallif : Shomansurov Oybek 
"""
# avtolar=['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar:
#     if avto=='bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# javob=float(input("12x6 nechiga teng? "))
# if javob!=72:
#     print("Javob xato !")
# else:
#     print("Javobingiz to'g'ri.")
    
# yosh=int(input("Yoshingiz nechida? "))
# if yosh>=18:
#     print("Xush kelibsiz !")
# else:
#     print("Kirish mumkin emas !")
    
# yil=int(input("Tug'ilgan yilingizni kiriting: "))
# if 2022-yil<18:
#     print(f"Yoshingiz {2022-yil} da ekan.")    
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")
    
# login=input("Yang login tanlang ")
# if len(login)<=5: 
#     print("Login 5 harfdan ko'proq bo'lishi shart")
    
cars=['toyota','mazda','hyundai','gm','kia']
for car in cars:
    if car=='gm':
        print(car.upper())
    else:
        print(car.title())
    
cars=['toyota','mazda','hyundai','gm','kia']
for car in cars:
    if car!='gm':
            print(car.title())
    else:
            print(car.upper())
    
login=input("Login ismingizni kiriting: ")
if login=='admin':
    print("Xush kelibsiz, Admin.")
    print(input("Foydalanuvchilar ro'yxatini ko'rasizmi? "))
else:
    print(f"Xush kelibsiz, {login}")    

son1=float(input("Birinchi sonni kiriting: "))
son2=float(input("Ikkinchi sonni kiriting: "))
if son1==son2:print("Sonlar teng")

son=int(input("Istalgan sonni kiriting: "))
if son>0:
    print("Musbat son")
else:
    print('Manfiy son')

son3=float(input("Son kiriting: "))
if son>0:
    print(son3**(1/2))
else:
    print("Musbat son kiriting")








