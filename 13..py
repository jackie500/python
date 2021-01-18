#13. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma pontosan a megadott szám legyen!


ok = True
szam = int(input("Adj meg egy szamot: "))

for i in range(szam):
    if ok:
        print("0", end=" ")
        ok = False
    else:
        print("1", end=" ")
        ok = True


