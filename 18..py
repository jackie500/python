# 18. Írj egy Python függvényt, amely paraméterként kap 2 egész számot és visszatér a két szám által meghatározott zárt intervallumban található egész számok összegével! A programodban hívd is meg ezt az alprogramot!


def my_function(a, b):
    összeg = 0
    for i in range(a + 1, b):
        összeg = összeg + i

    print(összeg)


szam1 = int(input("szám1: "))
szam2 = int(input("szám2: "))

my_function(szam1, szam2)
