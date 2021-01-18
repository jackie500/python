# 8. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azokat a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!

szam = int(input("szám: "))

for i in range(szam, 0, -1):
    i = i - 1
    if i % 3 == 0:

        print(i)