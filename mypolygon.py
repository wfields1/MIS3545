import turtle

alex = turtle.Turtle()

print(alex)

#for i in range(4):
#    alex.fd(100)
#    alex.lt(90)

#def square(t):
#    for i in range(4):
#        t.fd(100)
#        t.lt(90)

#square(alex)

#def square(t, length):
#    for i in range(4):
#        t.fd(length)
#        t.lt(90)

#square(alex, 50)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

#polygon(alex, 50, 8)

import math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

#circle(alex, 50)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length /3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

#arc(alex, 50, 360)

def polyline(t, n, length, angle):
    for i in range(n):
        
turtle.mainloop()