#  28. Írj egy Python programot, amely a teknőcgrafika segítségével kirajzol egy „házikó” alakú ötszöget!

import turtle

ablak = turtle.Screen()
ablak.setup(400,400)
ablak.title("program_1")
fred = turtle.Turtle()

fred.fd(100)
for i in range(2):
    fred.left(120)
    fred.fd(100)
fred.left(30)
for i in range(3):
    fred.fd(100)
    fred.left(90)

ablak.exitonclick()






