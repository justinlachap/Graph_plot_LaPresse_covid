from collections import Counter
from string import punctuation

import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


def get_words(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, features="html.parser")
    text_div = (''.join(s.findAll(text=True)) for s in soup.findAll('ul'))
    c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))
    return c_div['virus'] + c_div['coronavirus'] + c_div['covid-19']


def january():
    for i in range(1, 32):
        link = "https://www.lapresse.ca/archives/2020/1/%d.php" % (i)
        list.append((i, get_words(link)))


def feb():
    for i in range(1, 30):
        link = "https://www.lapresse.ca/archives/2020/2/%d.php" % (i)
        list.append((i + 32, get_words(link)))


def march():
    for i in range(1, 32):
        link = "https://www.lapresse.ca/archives/2020/3/%d.php" % (i)
        list.append((i + 62, get_words(link)))


def april():
    for i in range(1, 31):
        link = "https://www.lapresse.ca/archives/2020/4/%d.php" % (i)
        list.append((i + 94, get_words(link)))


def may():
    for i in range(1, 32):
        link = "https://www.lapresse.ca/archives/2020/5/%d.php" % (i)
        list.append((i + 125, get_words(link)))


def june():
    for i in range(1, 27):
        link = "https://www.lapresse.ca/archives/2020/6/%d.php" % (i)
        list.append((i + 157, get_words(link)))


list = []
january()
feb()
march()
april()
may()
june()
x = []
y = []
for i in range(len(list)):
    x.append(list[i][0])
    y.append(list[i][1])

plt.plot(x, y, 'r')
plt.vlines(x=30, ymin=0, ymax=50, linestyles='--', colors='#D3D3D3')
plt.vlines(x=60, ymin=0, ymax=50, linestyles='--', colors='#D3D3D3')
plt.vlines(x=90, ymin=0, ymax=50, linestyles='--', colors='#D3D3D3')
plt.vlines(x=120, ymin=0, ymax=50, linestyles='--', colors='#D3D3D3')
plt.vlines(x=150, ymin=0, ymax=50, linestyles='--', colors='#D3D3D3')
plt.text(54 + 7, -10, 'Données utilisées: lapresse.ca/archives/')
plt.xlabel('Jours de 2020')
plt.ylabel('Nombre d\'articles par jour')
plt.suptitle('Nombre d\'articles quotidiens à propos du Coronavirus publiés dans le journal La Presse durant la première moitié de 2020',
             fontsize=13, y=0.96)
plt.show()
