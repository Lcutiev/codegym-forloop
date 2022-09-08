import turtle as t
screen = t.Screen()
t.bgcolor("black")
t.title("Square")

pen = t.Turtle()
pen.speed()
pen.color("red")

for i in range(4):
	pen.forward(100)
	pen.left(90)

t.done()