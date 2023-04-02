"""
08.02.2022

Dasturlash asoslari

34-dars : JSON

Muallif : Shomansurov Oybek 
"""

import json

# json.dumps()
x=10
x_json=json.dumps(x)

y=5.5
y_json=json.dumps(y)


m=True
m_json=json.dumps(m)

sonlar=(12,45,23,67)
sonlar_json=json.dumps(sonlar)

bemor={
       "ism":"Alijon Valiyev",
       "yosh": 30,
       "oila": True,
       "farzandlar": ("Ahmad","Bonu"),
       "allergiya": None,
       "dorilar": [
         {"nomi": "Analgin", "miqdori": 0.5},
         {"nomi": "Panadol", "miqdori": 1.2}
      ]
    }

bemor_json=json.dumps(bemor,indent=3)
print(bemor_json)

# json.dump(x,fayl)
with open('bemor.json','w') as f:
    json.dump(bemor,f)

bemor2=json.loads(bemor_json)

