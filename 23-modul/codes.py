"""
23.01.2022

Dasturlash asoslari

23-dars : Modullar

Muallif : Shomansurov Oybek 
"""

# Modulni chiqarib olish
import avto_info_mod
avto1=avto_info_mod.avto_info("GM","Malibu","Qora",
                              "avtomat",2020,40000)
avto_info_mod.info_print(avto1)

import avto_info_mod as aim
avto1=aim.avto_info("GM","Malibu","Qora",'avtomat',2020,40000)

# Modul ichidan ma'lum funksiyalarni chaqirib olish
from avto_info_mod import avto_info , info_print
avto1=avto_info("GM","Malibu","Qora","avtomat",2020,40000)
info_print(avto1)

# Funksiyaga qisqa nom berish
from avto_info_mod import avto_info as ainfo
from avto_info_mod import info_print as iprint
avto1=ainfo("GM","Malibu","Qora",'avtomat',2020,40000)
iprint(avto1)

# Modul icidagi barcha funksiyalarni chaqirib olish
from avto_info_mod import *
avto1=ainfo("GM","Malibu",'Qora','avtomat',2020,40000)
info_print(avto1)