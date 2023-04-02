"""
26.01.2022

Dasturlash asoslari

24-dars : Lambda , map(), filter() funksiyalari

Muallif : Shomansurov Oybek 
"""

# map() funksiyaysi
# from math import sqrt 
# sonlar=list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# ildizlar=list(map(sqrt,sonlar))

# sonlar=list(range(11))
# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

# print(list(map(daraja2,sonlar)))

# kvadratlar=list(map(lambda x:x*x,sonlar))
# print(kvadratlar)

# kvadratlar=[]
# for son in sonlar:
#     kvadratlar.append(son*son)

a=[4,5,6]
b=[7,8,9]
a_plus_b=list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

ismlar=['hasan','husan','olim','umid']
print(list(map(lambda matn:matn.upper(),ismlar)))