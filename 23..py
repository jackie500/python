# 23. Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig, amíg a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában, majd írja ki a képernyőre a lista elemeit fordított sorrendben!

szam = int(input("szám: "))
lista = []

while szam != 0:
    lista.append(szam)
    szam = int(input("szám: "))

print(lista[::-1])











