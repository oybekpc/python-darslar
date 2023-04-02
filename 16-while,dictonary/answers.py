"""
17.01.2022

Dasturlash asoslari

18-dars : While , Ro'yxatlar , Lug'atlar

Muallif : Shomansurov Oybek 
"""
savat =[]
while True:
    mahsulot = input("Savatga mahsulot qo'shing:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
    if javob != 'ha':
        break

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")