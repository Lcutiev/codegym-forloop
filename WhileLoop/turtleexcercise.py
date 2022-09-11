# Import thư viện đồ họa turtle
from itertools import count
import turtle as t
# Import thư viện sinh số ngẫu nhiên
import random as r

# khởi tạo turtle
pen = t.Turtle()
pen.shape("turtle")

# Ẩn hình ảnh rùa
pen.hideturtle()
pen.pensize(3)
pen.color("blue")
pen.speed(1)
pen.penup()

# đặt rùa về phía trái màn hình

# cho rùa di chuyển từ trái qua phải
count = 0
while count < 10:
    # sinh hai giá trị ngẫu nhiên
    down = r.randint(20,50)
    up = r.randint(20,50)
    t.pendown()
    # rùa tiến về phía trước với giá trị ngẫu nhiên ở trên, có để lại nét vẽ
    t.forward(down)
    t.penup()
    # rùa tiến về phía trước với giá trị ngẫu nhiên ở trên, không để lại nét vẽ
    t.forward(up)
    count += 1
t.done()

import numpy

