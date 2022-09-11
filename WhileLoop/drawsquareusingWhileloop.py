import turtle as t
screen = t.Screen()
t.bgcolor("black")

pen = t.Turtle()
pen.speed()
pen.pencolor("Red")

edge = 0
while edge < 4:
    edge += 1
    pen.forward(100)
    pen.left(90)
t.done()