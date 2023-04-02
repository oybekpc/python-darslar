"""
16.01.2022

Dasturlash asoslari

12-dars :  Lug'at va to'plam

Muallif : Shomansurov Oybek 
"""
onam={'ism':"Go'zal","tugilgan":1985,"shahar":"Toshkent viloyati",'kasbi':"Tortchilik"}
print(f"Onamning ismi {onam['ism']} ,{onam['tugilgan']}-yilda , {onam['shahar']}da tug'ilgan")

taom={
      'Ali':'Osh',
      'Vali':'Makaron',
      'Hasan':"Sho'rva",
      'Husan':"Moshho'rda",
      'Olim':"Xonim"}
 
taom=taom['Ali']
print(f"Alining sevimli taomi {taom}")

lugat={'integer':'butun son',
       'float':"o'nlik son",
       'tuple':'ozgarmas qiymat',
       'varailables':'ozgaruvchilar',
       'dictionary':'lugat',
       'for':'uchun',
       'if':'agar',
       'else':'aks holda',
       'string':'matn',
       'list':"ro'yxat"}

kalit = input("Kalit so'z kiriting:").lower()
tarjima = lugat.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    






