# 14. Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott értékek között helyezkednek el!

szam1 = int(input("kisseb szám: "))
szam2 = int(input("nagyobb szám: "))

for i in range(szam1 + 1, szam2):
    print(i)