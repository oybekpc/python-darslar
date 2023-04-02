"""
08.01.2022

Dasturlash asoslari

06-dars : Sonlar

Muallif : Shomansurov Oybek 
"""
a=20 # Sonlar musbat 
b=-30 # Manfiy yoki
c=0 # 0 ga teng bo'lishi mumkin 
d=a+b
print(d)

# Kvadratning yuzini hisoblaymiz
kvdrt_tmni=20 # Kvadratning tomoni 20 ga teng 
kvdrt_yuzi=kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
print(kvdrt_yuzi)

pi=3.14159 # O'nlik son (float)
radius=10 # Butun son (integer)
diametr=2*radius
print("Aylana uzunligi", pi*diametr ,"ga teng .")

a=-20
b=40
c=b/a
print(c) # Natija o'nlik son bo'ladi

a=2 # Butun son 
b=3.0 # O'nlik son
print(a+b)
print(a*b)
print(a**b)
print(2*(a+b))

aholi=34_580_000
print(f"O'zbekiston aholisi {aholi} dan ortiq")

#Konstanta
PI=3.14159
radius=21.2

x,y,z=10,-7.25,-30 # x 10 ga , y -7.25 ga , z -30 ga teng

yosh,ism=15,"Oybek"
print(f"{ism.title()} {yosh} yoshda")

ism="Jobir"
yosh=36
xabar=ism + ' ' + str(yosh) +' '+'yoshda'
print(xabar)

t_yil=int(input("Tug'ilgan yilingizni kiriting: "))
yosh=2022-t_yil
print(f"Sizning yoshingiz {yosh}")
