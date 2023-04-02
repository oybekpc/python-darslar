"""
13.01.2022

Dasturlash asoslari

11-dars : Bir nechta shartlarni tekshirish 

Muallif : Shomansurov Oybek 
"""
# son=int(input("Son kiriting: "))
# if son>0: # agar son 0 dan katta bo'lsa
#     print("Son musbat")
# elif son<0: # aks holda , agar son 0 dan kichik bo'lsa,
#     print("Son manfiy")
# else: # aks holda
#     print("Son 0 ga teng")

# yosh=int(input("Yoshingiz nechida? "))
# if yosh<=4:
#     print("Sizga kirish bepul.")
# elif yosh<=12:
#     print("Sizga kiriish 5000 so'm")
# else:
#     print("Sizga kirish 10000 so'm")

# yosh=int(input("Yoshingiz nechida? "))
# if yosh<12:
#     print("Sizga kirish 5000 so'm.")
# elif yosh<4:
#     print("Sizga kirish bepul.")
# else:
#     print("Sizga kirish 10000 so'm")

# yosh=int(input("Yoshingiz nechida? "))
# if yosh<=4:
#     price='tekin'
# elif yosh<=12:
#     price=5000
# elif yosh<65:
#     price=10000
# else:
#     price=5000
# print(f"Sizga kirish {price} so'm")

# kun=input("Bugun nima kun? ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni.")

#print(True or False)
# kun=input("Bugun nima kun? ")
# harorat=float(input("Havo harorati qanday? "))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")

# narx=15000 # mijoz 15000 so'mga taom oladi 
# choy=True
# salat=False

# if choy and salat:# agar mijoz choy va salat olgan bo'lsa
#     narx=narx+10000 # narxga 10000 so'm qo'shamiz 
# elif choy or salat:# agar choy yoki salat olgan bo'lsa
#     narx=narx+5000 # narxga 5000 so'm qo'shamiz
# print(f"Jami {narx} so'm ") # yakuniy narxni chiqaramiz

# narx=15000
# choy=True
# salat=False
# non=True
# kampot=True
# assorti=False

# if choy:
#     print("Mijoz choy oldi.")
#     narx=narx+3000
# if salat:
#     print("Mijoz salat oldi.")
#     narx=narx+5000
# if non:
#     print("Mijoz non oldi.")
#     narx=narx+2000
# if kampot:
#     print("Mijoz kampot oldi.")
#     narx=narx+5000
# if assorti :
#     print("Mijoz assorti oldi.")
#     narx=narx+15000
# print(f"Jami {narx} so'm.")

# in operatori
# menyu=['osh','qozonkabon','shashlik','norin','somsa']
# 'manti' in menyu
# 'osh' in menyu

# menyu=['osh','qozonkabon','shashlik','norin','somsa']
# ovqat=input("Nima ovqat yeysiz? ")
# if ovqat.lower() in menyu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Afsuski, bizda bunday ovqat yo'q.")

# menyu=['osh','qozonkabon','shashlik','norin','somsa']
# ovqat=input("Nima ovqat yeysiz? ")
# if ovqat.lower() not in menyu:
#     print("Afsuski, bizda bunday ovqat yo'q.")
# else:
#     print("Buyurtma qabul qilindi.")
    
# menyu=['osh','qozonkabon','shashlik','norin','somsa']
# buyurtmalar=["osh",'somsa','manti','shashlik']
    
# for taom in buyurtmalar:
#     if taom in menyu:
#         print(f"Menyuda {taom} bor")
#     else:
#         print(f"Kechirasiz menyuda {taom} taom yo'q.")
    
# list1=[1,2,3]
# if list1: #Bu ifoda True qaytaradi,sababi list1 bo'sh emas
#     print("Ro'yxatda element bor")

# menyu=['osh','qozonkabon','shashlik','norin','somsa']
# buyurtmalar=["osh",'somsa','manti','shashlik']
    
# for taom in buyurtmalar:
#     if taom in menyu:
#         print(f"Menyuda {taom} bor")
#     else:
#         print(f"Kechirasiz menyuda {taom} taom yo'q.")
# else:        
#      print("Savatchangiz bo'sh.")   