import turtle
from exercise3 import draw_square
for i in range(30):
    f= turtle.Pen()
    draw_square(i * 5, 'red')
    f.left(17)
    f.penup()
    f.forward(i * 2)
    f.pendown()
f.done()
