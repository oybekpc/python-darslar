"""
10.01.2022

Dasturlash asoslari

08-dars : Ro'yxatlar bilan ishlash

Muallif : Shomansurov Oybek 
"""
# sort() metodi
cars=['bmw','volvo','gm','tesla','audi',]
cars.sort()
print(cars)

cars=['bmw','volvo','GM','tesla','audi',]
cars.sort()
print(cars)

cars=['bmw','volvo','gm','tesla','audi',]
cars.sort(reverse=True)
print(cars)

mehmonlar=['Odil','Hamid','Temur','Avazbek','Farrux']
print("sorted() qaytargan ro'yxat:",sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:",mehmonlar)

print(sorted(mehmonlar,reverse=True))

ages=[12,98,34,65,43,34,76,11]
ages.sort()
print(ages)
print(sorted(ages,reverse=True))

fruits=['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)

fruits=['pear','banana','apple','watermelon','lemon']
print("Elementlar soni:", len(fruits))

sonlar=list(range(0,10))
print(sonlar)

juft_sonlar=list(range (0,20,2)) # 0 dan 20 gacha 2 qadam bilan 
toq_sonlar=list(range(1,20,2))
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar )

narxlar=[12000,22500,23456,9800,5600,9934,32874]
arzon=min(narxlar)
qimmat=max(narxlar)
jami=sum(narxlar)
print("Eng arzon narx:",arzon,\
      ".Eng qimmat narx:",qimmat,\
          ".Jami:",jami)\

cars=['bmw','volco','gm','toyota','tesla','audi']
my_cars=cars[0:3]
print(my_cars)

print(cars[2:5])
print(cars[:4])
print(cars[2:])

sonlar=[1,2,3,4,5,6,7]
sonlar2=sonlar
sonlar2.append(9)
sonlar2.append(8)
print("Bu sonlar ro'yxati:",sonlar)
print("Bu sonlar2 ro'yxati:",sonlar2)

sonlar=[1,2,3,4,5,6,7]
sonlar2=sonlar[:]
sonlar2.append(9)
sonlar2.append(8)
print("Bu sonlar ro'yxati:",sonlar)
print("Bu sonlar2 ro'yxati:",sonlar2)

# Tuples (O'zgarmas ro'yxatlar)
tomonlar=(20,30,40,55.2)
print(tomonlar)

toys=['bus','car','bear','dino','snake','lizard']
print(toys[0])
print(toys[-1])
print(toys[2:5])
toys=['bus','car','bear','dino','snake','lizard']
toys[3]='dragon'
print(toys)

toys=list(toys) 
toys.append('dragon')
toys.remove('bus')
toys[1]='mcqueen'
toys=tuple(toys)
print(toys)