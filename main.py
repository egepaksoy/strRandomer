from random import choice

def getRand(word):
    x = 0
    kelimenin_indexleri = []
    while x < len(word):
        kelimenin_indexleri.append(x)
        x+=1

    yeni_kelime = ""

    while len(kelimenin_indexleri) > 0:
        y = choice(kelimenin_indexleri)
        yeni_kelime += word[y]
        kelimenin_indexleri.pop(kelimenin_indexleri.index(y))

    return kelimenin_indexleri

print(getRand("açık"))
