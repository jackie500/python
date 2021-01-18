#15. Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre a csillag (*) karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!

def myfun(n, m):
    for a in range(m):
        for b in range(n):
            print("*", end=" ")
        print("")

myfun(3, 5)

# itt inputtal kell megadni a csillagok számát:

"""
def myfun(n, m):
    for a in range(m):
        for b in range(n):
            print("*", end=" ")
        print("")
szam1 = int(input("szám1: "))
szam2 = int(input("szám2: "))
myfun(szam1, szam2)

"""


