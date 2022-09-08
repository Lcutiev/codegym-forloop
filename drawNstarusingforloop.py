import turtle as t

screen = t.Screen()
t.bgcolor("black")
t.title("Star")

pen = t.Turtle()
pen.speed(0)
pen.color("Red")

for j in range (1, 100):
    for i in range(1, 6):
        pen.left(144)
        pen.forward(200)
    pen.left(5)
t.done()