# 16. Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap egy egész számot és eldönti a számról, hogy osztható-e 2-vel és 3-mal is egyszerre! A programodban hívd is meg ezt az alprogramot!


def myfun(a):
    if szam % 2 == 0 and szam % 3 == 0:
        print("igen ")
    else:
        print("nem")
szam = int(input("szám: "))


myfun(szam)












