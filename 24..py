# 24. Írj egy Python programot, amely megmondja előfordul-e (igen/nem) a Debrecen szó a temp.txt fájlban!



szoveg = open("temp.txt")
szoveg = szoveg.read()

#print(szoveg)
if "Debrecen" in szoveg:
    print("Igen")
else:
    print("Nem")



