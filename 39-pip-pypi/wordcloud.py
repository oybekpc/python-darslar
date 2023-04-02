"""
19.02.2022

Dasturlash asoslari

39-dars : PYTHON Tashqi Kutubxonasi

Muallif : Shomansurov Oybek 
"""

import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotib.pyplot as plt

sahifa="https://kun.uz/news/main"
r=requests.get(sahifa)

soup=BeautifulSoup(r.text,'html.parser')
news=soup.find_all(class_="new-title")
print(news[0].text)
matn=''
for n in news:
    matn += n.text

stopwords=["учун","бўйича","лекин","билан","ва","бор","ҳам","хил","йил"]
wordcloud = WordCloud(width=1000,height=1000,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=20).genetare(matn)

plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()