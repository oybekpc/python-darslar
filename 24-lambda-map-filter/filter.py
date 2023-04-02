"""
26.01.2022

Dasturlash asoslari

24-dars : Lambda , map(), filter() funksiyalari

Muallif : Shomansurov Oybek 
"""

# filter() funksiyasi
# import random as r
# sonlar=r.sample(range(100),10)
# def juftmi(x):
#     """x juft bo'lsa,True, aks holda,False qaytaramiz"""
#     return x%2==0

# juft_sonlar=list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)

# import random as r

# sonlar=r.sample(range(100),10)
# juft_sonlar=list(filter(lambda son:son%2==0,sonlar))

# print(sonlar)
# print(juft_sonlar)

# mevalar=['olma','anor','anjir','qovun','banan',"o'rik"]
# mevB=list(filter (lambda meva:meva.startswith('b'),mevalar))
# print(mevB)

# mevalar2=list(filter(lambda meva:len(meva)<=4,mevalar))
# print(mevalar2)

# list(filter(lambda meva:(meva.startswith('a') and \
#                          meva.endswith('r')),mevalar))