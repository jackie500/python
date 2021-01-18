# 27. Írj egy Python programot, amely a teknőcgrafika segítségével egy ötágú sárga csillagot rajzol ki!


import turtle

ablak = turtle.Screen()
ablak.setup(400,400)
ablak.bgcolor('white')
ablak.title("program_3")
fred = turtle.Turtle()
for i in range(5):
    fred.fd(100)
    fred.right(144)
ablak.exitonclick()








"""
ablak = turtle.Screen()
ablak.setup(400,400)
ablak.bgcolor('white')
ablak.title("program_3")
fred = turtle.Turtle()
for i in range(5):
    fred.fd(100)
    fred.right(144)
ablak.exitonclick()
"""
