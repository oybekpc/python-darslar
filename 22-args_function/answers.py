"""
22.01.2022

Dasturlash asoslari

22-dars : Moslanuvchan finksiya(*args,**kwargs)

Muallif : Shomansurov Oybek 
"""

# def sonlar_qabul_qil(*sonlar):
#     kopaytma=1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma

# print(sonlar_qabul_qil(4,5,6))

def talaba(ism,familiya,**kwargs):
    kwargs['ism']='ism'
    kwargs['familiya']='familiya'
    return kwargs

talaba_info=talaba('oybek','shomansurov',maktab=2)


