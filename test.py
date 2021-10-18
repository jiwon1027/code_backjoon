import turtle
t = turtle.Pen()

list = [50,100,200]

for x in list:
    t.circle(x)
    t.left(90)
    t.circle(x)
    t.right(90)
