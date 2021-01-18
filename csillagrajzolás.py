
#def harmadikplussz(number):
#    for i in range(1,number+1):
#        if i % 3 == 0:
#            print("+", end="")
#        else:
#            print("-", end="")

#harmadikplussz(10)

for i in range(1,100+1):
    if i % 5 == 0:
        print("*", end="")
    else:
        print("-", end="")

#Használj két for ciklust, egyiket a másikba ágyazva, ahhoz, hogy megkapd az alábbi 10x10-s négyszöget:
for row in range(10):
    for column in range(10):
        print("*", end=" ")

    # Print a blank line for next row
    print()
