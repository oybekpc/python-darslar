"""
12.01.2022

Dasturlash asoslari

10-dars : if-else 

Muallif : Shomansurov Oybek 
"""
a=5
b=6
print(a==b) # a b ga teng(mi?)
#False

a=6
b=5
print(b==(a-1))
#True

print(10**2<2**10)
#True

ism='ahad'
print(ism!='Ahad')
print(ism.title()=='Ahad')
nums1=[1,2,3]
nums2=[1,2,4]
print(nums1!=nums2)
print(9**2>=7*9+18)
x=10
# print(x*x<'x**2')
# print(x*x>=float(f"{x**2}"))

# if-else
son=int(input("Istalgan sonni kiriting: "))
if son>0:
    print(son,"musbat son")

yosh=int(input("Yoshingizni kiriting: "))
if yosh<7:
    print("Sizga avtobus bepul")
else:
    print("Chipta narxi 5000 so'm")

yosh=int(input("Yoshingiz nechida? "))
if yosh>65: print("SiZ COVID 19 risk guruhida ekansiz.")

x,y=25,50 # x=25 y=50 
if x>y:
    print("x>y")
else:
    print("x<y")

ism="Ali"
ism.lower()=='ali'
