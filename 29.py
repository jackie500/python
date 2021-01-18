# 29. Írj egy Python programot, amely a teknőcgrafika segítségével kirajzol egy 30, 40 és 50 egység oldalhosszúságú derékszögű háromszöget!

import turtle

ablak = turtle.Screen()
ablak.setup(400,400)
ablak.title("program_1")
fred = turtle.Turtle()
fred.left(90)
fred.fd(300)
fred.right(126.86)
fred.fd(500)
fred.right(143.1301)
fred.fd(400)

ablak.exitonclick()





