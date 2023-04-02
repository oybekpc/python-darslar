"""
16.01.2022

Dasturlash asoslari

16-dars : Nesting

Muallif : Shomansurov Oybek 
"""
gazzoliy={'ism':"Abu Xomid G'azzoliy",
          'tyil':1058,
          'vyil':1111,
          'tjoy':'Eron',
          'asarlar':["Ihya ulum ad-din (\"Diniy ilimlarni tiriltirish\")","al-adab fid-din(\"Musulmon odolari\")"]}
ibn_sino={'ism':'Abu ali ibn sino',
          'tyil':980,
          'vyil':1037,
          'tjoy':'Buxoro',
          'asarlar':["Alhikmat al-Aruziy"]
          }
navoiy={'ism':'Alisher Navoiy',
        'tyil':1441,
        'vyil':1501,
        'tjoy':'Hirot',
        'asarlar':["Xamsa","Majnun va Layli"]}
amir={'ism':'Amir Temur',
      'tyil':1336,
      'vyil':1405,
      'tjoy':'Kesh',
      'asarlar':["Amir Temur tuzuklari"]}

mashhurlar=[gazzoliy,ibn_sino,navoiy,amir]

for mashhur in mashhurlar:
    ism=mashhur['ism']
    asarlar=mashhur['asarlar']
    tyil=mashhur['tyil']
    vyil=mashhur['vyil']
    tjoy=mashhur['tjoy']
    print(f"{ism} {tyil}-yilda {tjoy} da tavallud topgan. Asarlari {asarlar} "
          f"{vyil-tyil}  yoshida olamdan o'tgan")

kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)
    
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
davlat=input("Davlat nomini kiriting: ")
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:    
    print("Bizda bu davlat haqida malumot mavjud emas.")
    
