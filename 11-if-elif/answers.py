"""
13.01.2022

Dasturlash asoslari

11-dars : Bir nechta shartlarni tekshirish 

Muallif : Shomansurov Oybek 
"""
# son=float(input("Juft son kiriting: "))
# if son%2:
#     print("Bu juft son emas.")
# else:
#     print("Rahmat!")

# yosh=float(input("Yoshingizni kiriting: "))
# if yosh<4 or yosh<=60:
#     narx='tekin'
# elif yosh<18:
#     narx=10000 
# else:
#     narx=20000
# print(f"Sizga kirish {narx} ")

# son1=float(input("Birinchi sonni kiriting: "))
# son2=float(input("Ikkinchi sonni kiriting: "))
# if son1==son2:
#     print("Ikki son bir-biriga teng.")
# elif son1>son2:
#     print(f"{son1} soni {son2} dan katta.")
# else:
#     print(f"{son1} soni {son2} dan kichik.")

# x=float(input("Birinchi sonni kiriting: "))
# y=float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x>y:
#     print(f"{x}>{y}")
# else:
#     print(f"{x}<{y}")

# mahsulotlar=['xurmo','sabzi','kartoshaka','piyoz',
#              'pomidor','no\'hot','karam','guruch','yog\'','banan']
# savat=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni kiriting: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print("Mahsulot do'konimizda bor .")
#     else:print("Mahsulot do'konimizda yo'q .")

# mahsulotlar=['xurmo','sabzi','kartoshka','piyoz',
#              'pomidor','no\'hot','karam','guruch','yog\'','banan']
# savat=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni kiriting: "))

# bor_mahsulotlar=[]
# mavjud_emas=[]
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q: ")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlat do'konimizda bor")

# foydalanuvchilar=['oybek','ozodbek','sunnat','javohir','diyor']
# login=input("Yangi login tanlang: ")

# if login.lower() in foydalanuvchilar:
#     print(input("Bu login band, boshqa login kiriting. "))
# else:
#     print(f"{login} , Xush kelibsiz!")
    
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")