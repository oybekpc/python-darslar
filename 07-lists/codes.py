"""
09.01.2022

Dasturlash asoslari

07-dars : Lists (Ro'yxatlar)

Muallif : Shomansurov Oybek 
"""
mevalar=['olma','anjir','shaftoli',"o'rik"]
narxlar=[12000,18000,10900,22000]
sonlar=['bir','ikki',3,4,5] # <- aralash ro'yxat
ismlar=[] # Bo'sh ro'yxat
print("Birinchi meva:",mevalar[0].title())
print("Ikkinchi meva:",mevalar[1].title())
print("Oxirgi meva:",mevalar[3].title())

narxlar=[1200,18000,10900,22000]
print(narxlar[2]+narxlar[3])

numbers=[10,12,345,-23,445,61,-45,56,-34]
print(numbers[-1])

narxlar=[12000,18000,10900,22000]
narxlar[0]=13000 # 1-qiymatni 13000 ga o'zgartiramiz
narxlar[2]=11000 # 3-qiymatni 11000 ga o'zgartiramiz
narxlar[3]=narxlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narxlar)

# append()
mevalar=["olma","anjir","shaftoli","o'rik"]
mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz 
mevalar.append("banan")
print(mevalar)

cars=[]
cars.append("Lacetti") # Ro'yxatga Lacetti qo'shamiz
cars.append("Malibu") # Ro'yxatga Malibu qo'shamiz 
cars.append("Cobalt") #Ro'yxatga Cobalt qo'shamiz 
print(cars)

# Insert() 
cars=['Lacetti','Malibu','Cobalt']
print(cars)
cars.insert(0,'Spark')
print(cars)
cars.insert(2,'Damas')
print(cars)

# del
mevalar=["olma","anjir","shaftoli","o'rik",'anor']
del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
print(mevalar)

# remove()
mevalar=['olma','anjir','shaftoli',"o;rik",'anor']
mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
print("mevalar")

#pop.()
hayvonlar=['it','mushuk','sigir','quyon','mushuk']
hayvonlar.pop(1)
print(hayvonlar)