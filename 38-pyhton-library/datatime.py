"""
16.02.2022

Dasturlash asoslari

38-dars : PYTHON  Kutubxonasi

Muallif : Shomansurov Oybek 
"""

# import datetime as dt


# datetime
# hozir = dt.datetime.now()
# print(hozir)
# Sanani ajratib olish
# print(hozir.date())
# Vaqtni ajratib olish
# print(hozir.time())
# Soatni ajratib olish
# print(hozir.hour)
# Minutni ajratib olish
# print(hozir.minute)
# Sekundni ajratib olish
# print(hozir.second)

# date()
# bugun=dt.date.today()
# print(f"Bugungi sana: {bugun}")
# ertaga=dt.date(2022,2,17)
# print(f"Ertangi sana: {ertaga}")

# time()
# hozir=dt.datetime.now()
# vaqtHozir=hozir.time()
# print(f"Hozir soat: {vaqtHozir}")
# vaqtKeyin=dt.time(23,45,30)
# print(vaqtKeyin)

# Sanalar orasida farq
# bugun=dt.date.today()
# ramazon=dt.date(2022,4,13)
# farq=ramazon-bugun
 # print(farq)
# print(f"Ramazonga {farq.days} kun qoldi")

# Soatlar orasida farq
# hozir = dt.datetime.now()
# futbol = dt.datetime(2022,3,10,23,45,00)
# farq = futbol-hozir
# sekundlar=farq.seconds
# minutlar=int(sekundlar/60)
# soatlar=int(minutlar/60)
# print(f"Futbol boshlanishiga {farq.days} kunu {soatlar} soat {minutlar} minut {sekundlar} sekund qoldi.")