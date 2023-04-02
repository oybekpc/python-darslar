"""
29.01.2022

Dasturlash asoslari

25-dars : "Son topish o'yini" 

Muallif : Shomansurov Oybek 
"""

import random

def sontop(x=10):
    tasodifiy_son=random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim topa olsizmi ?")
    taxminlar=0
    while True:
        taxminlar+=1
        taxmin=int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato . Men o'ylagan son bundan kattaroq. Yana haraka qiling")
        elif taxmin>tasodifiy_son:
            print("Xato . Men o'ylagan son bundan kichikroq. Yana haraka qiling")
        else:
            print(f"Tabriklaymiz. {taxminlar} ta taxmin bilan topdingiz!")
            return taxminlar
            break
    
    
def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugamni bosing.Men topaman.")
    quyi=1
    yuqori=x
    taxminlar=0
    while True:
        taxminlar += 1
        if quyi!=yuqori:
            taxmin=random.randint(quyi,yuqori)
        else:
            taxmin=quyi
        javob=input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t),"
                    f"men o'ylagan son bundan kattaroq(+), yoki kichikroq(-)".lower())
        if javob =="-":
            yuqori = taxmin - 1
        elif javob=="+":
              quyi = taxmin + 1
        else:
            break 
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar
        
def play(x=10):
    yana=True
    while yana:
        taxminlar_user=sontop(x=10)
        taxminlar_pc=sontop_pc(x=10)
        
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim")
            break
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz")
            break
        else:
            print("Durrang!")
            break
            yana=int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0): "))