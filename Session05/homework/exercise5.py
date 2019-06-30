import turtle
def draw_star(x,y,length):
    f = turtle.Pen()
    f.speed(3)
    f.setpos(x,y)

    for i in range(4):
        f.forward(length)
        f.right(144)    
    f.done()
draw_star(100,150,200)
# chưa ok