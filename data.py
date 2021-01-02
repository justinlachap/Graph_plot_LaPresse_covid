from collections import Counter
from string import punctuation

import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

KEYWORDS = ['virus', 'coronavirus', 'covid-19']


def get_words(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, features="html.parser")
    text_div = (''.join(s.findAll(text=True)) for s in soup.findAll('ul'))
    c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))
    return c_div[KEYWORDS[0]] + c_div[KEYWORDS[1]] + c_div[KEYWORDS[2]]


# days per month
months = {'january': 31, 'feb': 29, 'march': 31, 'april': 30, 'may': 31, 'june': 30}

list, index = [], 1
for i in months.values():
    for j in range(1, i + 1):
        link = f"https://www.lapresse.ca/archives/2020/{index}/{j}.php"
        list.append((j + index * i, get_words(link)))
        index += 1

x, y = [], []
for i in range(len(list)):
    x.append(list[i][0])
    y.append(list[i][1])

plt.plot(x, y, 'r')
for i in [30, 60, 90, 120, 150]:
    plt.vlines(x=i, ymin=0, ymax=50, linestyles='--', colors='#D3D3D3')
plt.text(54 + 7, -10, 'Données utilisées: lapresse.ca/archives/')
plt.xlabel('Jours de 2020')
plt.ylabel('Nombre d\'articles par jour')
plt.suptitle(
    'Nombre d\'articles quotidiens à propos du Coronavirus publiés dans le journal La Presse durant la première moitié de 2020',
    fontsize=13, y=0.96)
plt.show()
