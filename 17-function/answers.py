"""
05/01/2022

Dasturlash asoslari

19-dars : Funksiya

Muallif : Shomansurov Oybek 

"""


def tugilgan_y(ism,yosh,j_yil=2022):
    print(f"{ism.title()} {j_yil-yosh} yilda tug'ilgan.")

tugilgan_y('oybek',15)

def hisoblab_ber(son):
    """Sonning kvadrati va kubini hisoblovchi fuksiya"""
    print(f"{son} ning kvadrati {son**2} ga , kubi {son**3} ga teng")

hisoblab_ber(6)

def son_qabul_qiluvchi(son):
    """Foydalanuvchidan son qabul qilib sonning juft yoki toqligini aniqlovchi funksiya""" 
    if son%2:
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")

son_qabul_qiluvchi(239876)
son_qabul_qiluvchi(1457)

def kattami_kichikmi(a,b):
    """sonlarni solishtiruvchi funksiya """
    if a>b:
        print(f"{a}>{b}")
    elif a<b :
        print(f"{a}<{b}")
    else:
        print(f"{a}={b} sonlar teng")

kattami_kichikmi(10,20)
kattami_kichikmi(-2,-179)
kattami_kichikmi(2,2)

def bolamiz(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")