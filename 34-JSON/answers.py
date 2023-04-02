"""
08.02.2022

Dasturlash asoslari

34-dars : JSON

Muallif : Shomansurov Oybek 

Javoblar
"""
import json

#1
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
jdata=json.dumps(data,indent=4)
print(jdata)

# 2
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba=json.loads(talaba_json)
print(f"{talaba['ism']} , {talaba['familiya']}")

#3
# with open ("javoblar/data.json","w") as f:
#     json.dump(data,f)

# with open("javoblar/talaba.json","w") as f:
#     json.dump(talaba,f)

#4
with open("javoblar/wikipedia.json") as f:
    wiki = json.load(f)

print(wiki["query"]["pages"]["13801"]["title"])
print(wiki["query"]["pages"]["13801"]["extract"])
