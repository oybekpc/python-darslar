"""
10.02.2022

Dasturlash asoslari

35-dars : 

Muallif : Shomansurov Oybek 
"""

# yosh=input("Yoshingizni kiriting: ")
# yosh=int(yosh)
# print(f"Siz {2021-yosh} yilda tug'ilgansiz.")


# yosh=input("Yoshingizni kiriting: ")
# try:    
#     yosh=int(yosh)
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz.")
# except:
#     print("Siz butun son kiritmadingiz")


# yosh=input("Yoshingizni kiriting: ")

# try:    
#     yosh=int(yosh)
# except:
#     print("Siz butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz.")

 
# yosh=input("Yoshingizni kiriting: ")

# try:    
#     yosh=int(yosh)
# except ValueError:
#     print("Siz butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz.")


# ZeroDivisionError

# x,y=5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
    

# IndexError

# mevalar=['olma','anor','uzum','anjir']
# try:
#     print(mevalar[4])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")


# KeyError
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}


# key="tel"
# try:
#     print(f"Foydalanauvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas")

# print(user['username'])

# FilenotFoundError

# filename="data.txt"
# try:  
#     with open(filename) as f:
#        text=f.read()
# except FileNotFoundError:
#      print(f"{filename} mavjud emas")
     
# import json
# files=['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba=json.load(f)
#     except FileNotFoundError:
#          print(f"{filename} mavjud emas")
#     else:
#          print(talaba['ism'])


# n=input("Butun son kiriting: ")
# try:
#     n=int(n)
#     x=20/n
# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")
    

# while True:
#     yosh=input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh=int(yosh)
#         break
 
# print(f"Siz {2022-yosh} yilda tug'ilgansiz.")
