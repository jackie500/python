
"""
Írj egy Python programot, amely a szamok.txt fájlba írja a 100 legkisebb 3-mal osztható pozitív
egész számot!

"""


f = open("szamok.txt", "w")
i = 0
for i in range(1, 100):
    if i % 3 == 0:
        f.write(str(i) + " ")

    i = i + 1
f.close()

# while-al:
"""
f = open("szamok.txt", "w")
db = 0
i = 3

while db != 100:
    if i % 3 == 0:
        f.write(str(i) + " ")
        db = db + 1
    i = i + 1
f.close()
"""
