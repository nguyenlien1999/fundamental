# 3 Write a Python function that draws a square, named draw_square, takes 2 arguments: length and color, 
# where length is the length of its side and color is the color of its bound (line color)
import turtle
def draw_square(size,colors):
  f = turtle.Pen()
  f.color(colors)
#   f.color(color)
  for i in range(3):
    f.forward(size)
    f.right(90)
  f.forward(size)
  f.done()
draw_square(200,"blue")


