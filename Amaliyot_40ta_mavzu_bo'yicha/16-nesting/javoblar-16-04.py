э"""
06/12/2020

Dasturlash asoslari

#16-dars: NESTING

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

с

for davlat, info in davlatlar.items():
    if davlat.lower()=='aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")