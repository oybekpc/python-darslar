"""
16.01.2022

Dasturlash asoslari

16-dars : Nesting

Muallif : Shomansurov Oybek 
"""
# car0={
#       'model':'lacetti','rang':'oq',
#       'yil':2018,'narx':13000,
#       'km':50000,'korobka':'avtomat'
#       }
# car1={
#       'model':'nexia3','rang':'qora',
#       'yil':2015,'narx':9000,
#       'km':89000,'korobka':'mexanika'
#       }
# car2={
#       'model':'gentra','rang':'qizil',
#       'yil':2019,'narx':15000,
#       'km':20000,'korobka':'mexanika'
#       }

# car=car0
# print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}-yil,{car['narx']}$")

# car=car1
# print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}-yil,{car['narx']}$")

# car=car2
# print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}-yil,{car['narx']}$")

# cars=[car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()},"
#           f"{car['rang']} rang,"
#           f"{car['yil']}-yil, {car['narx']}$")

# print(cars[0])
# print(cars[0]['model'])
# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")

# malibus=[]
# for n in range(10):
#     new_car={
#         'model':'malibu',
#         'rang':None,
#         'yil':2020,
#         'narx':None,
#         'km':0,
#         'korobka':'avto'
#         }
# malibus.append(new_car)
# print(malibus)
# for malibu in malibus[:3]:
#     malibu['rang']='qizil' 
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
# for malibu in malibus[6:]:
#     malibu['rang']='qora'
#     malibu['korobka']='mexanika'

# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narx']=40000
#     else:
#         malibu['narx']=35000

# for malibu in malibus:
#     print(malibu.values())

# dasturchilar={
#     'ali':['pyhton','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++',"c#"]    
#     }
# for ism,tillar in dasturchilar.items():
#      print(f"\n{ism.title()}:",end='')    
#      for til in tillar:
#          print(f"{til.upper()} ",end='')
         
# hamkasblar={
#     'ali':{'familiya':'valiyev',
#            't_yil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             't_yil':2001,
#             'malumot':"o'rta maxsus",
#             'tillar':['html','css','js']},
#    'hasan':{'familiya':'husanov',
#              't_yil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }
# for ism,info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()},"
#           f"{info['t_yil']}-yilda tug'ilgan.\n"
#           f"Ma'lumoti:{info['malumot']}. \n"
#           "Quyidagi dasturlash tillarni biladi:")
#     for til in info['tillar']:
#         print(til.upper())