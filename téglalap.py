import turtle

ablak = turtle.Screen()
ablak.setup(400,400)
ablak.bgcolor('white')
ablak.title("program_1")
fred = turtle.Turtle()
for i in range(2):
    fred.fd(100)
    fred.left(90)
    for j in range(1):
        fred.fd(50)
        fred.left(90)
ablak.exitonclick()