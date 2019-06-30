from turtle import *
from exercise5 import draw_star

f= Turtle.Pen()
f.speed(0)
f.color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
length = random.randint(3, 10)

draw_star(x, y, length)
f.done()
