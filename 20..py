# 20. Írj egy Python eljárást, amely paraméterként kap egy pozitív egész számot és kiír a képernyőre ennyi karaktert úgy, hogy minden harmadik karakter pluszjel (+) legyen a többi viszont mínuszjel (-)! A programodban hívd is meg ezt az alprogramot!

def myfun(a):

    for i in range(1, szám + 1):
        if i % 3 == 0:
            print("+", end=" ")

        else:
            print("-", end=" ")

szám = int(input("szám: "))
myfun(szám)



