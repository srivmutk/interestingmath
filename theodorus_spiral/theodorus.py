import turtle
from math import atan2, sqrt, cos, sin, atan

s = turtle.getscreen()
t = turtle.Turtle()
t.width(5)
t.hideturtle()

n =100
f=16

def rtop(x1,y1):
    adj = sqrt(x1**2 + y1**2)
    angle = atan(n/adj) + atan2(y1, x1)
    mag = sqrt(x1**2+y1**2+n**2)

    t.goto(x1,y1)
    t.goto(mag*cos(angle), mag*sin(angle))
    t.goto(0,0)

    return [mag*cos(angle), mag*sin(angle)]

p = list([rtop(n,0)])

for i in range(1, f):
    p.append(rtop(p[i-1][0], p[i-1][1]))

turtle.done() 