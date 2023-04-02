"""
08.02.2022

Dasturlash asoslari

34-dars : JSON

Muallif : Shomansurov Oybek 
"""

import json

filename='bemor.json'
with open(filename) as f:
    bemor=json.load(f)

print(type(bemor))
