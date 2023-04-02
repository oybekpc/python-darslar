"""
15.01.2022

Dasturlash asoslari

12-dars :  Lug'at va to'plam

Muallif : Shomansurov Oybek 
"""
car={'model':'ferari','rang':'qizil'}
print(car['model'])
print(car['rang'])

talaba={'ism':"murod olimov",'yosh':20,'t_yil':2000}
print(f"{talaba['ism'].title()},\
      {talaba['t_yil']}-yilda tug'ilgan,\
          {talaba['yosh']} yoshda")

car={
     'make':'GM',
     'model':'Malibu',
     'color':'Black',
     'gear':'Automatic',
     'year':2020,
     'price':40000
     }

print(car['model'])
color=car.get('narx','Bunday kalit mavjud emas')
print(color)

talaba['kurs']=4
talaba['fakultet']='informatika'
print(talaba)

cars={}
car['model']='Mazda 6'
car['color']='Red'
car['price']=40000
print(f"{car['color']} {car['model']},{car['price']}$")

car['price']=38000
print(f"{car['color']}{car['model']},{car['price']}$")

car={'Model':'Malibu','color':'Black','price':40000}
print(car)

del car['color']
print(car)





