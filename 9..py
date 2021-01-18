# 9. Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a képernyőre azokat a páros számokat, amelyek a két adott érték közötti zárt intervallumban találhatóak!

szam1 = int(input("szám 1:"))
szam2 = int(input("szám 2:"))
for i in range(szam1, szam2):
    if i % 2 == 0:
        print(i)