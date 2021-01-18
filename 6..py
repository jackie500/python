#6. Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a képernyőre, hogy mind a három páros szám-e (igen/nem)!

összeg = int(input("szám1: ")) + int(input("szám2: ")) + int(input("szám3: "))

if összeg % 2 == 0:
    print("igen")
else:
    print("nem")
#folytatni tovább: egyesével vizsgálja meg hoyg páros szám e
