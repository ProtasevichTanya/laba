import turtle as t
from random import *

t.shape('turtle')
t.color('blue')
t.width(3)
t.penup()

A0 = [ (0, 0, 1), (10, -90, 1), (20, -90, 1), (10, -90, 1), (20, -90, 0), (20, 0, 0) ]
A1 = [ (0, -90, 0), (10, 45, 1),(14, 135, 1), (20, 270, 0), (10, 0,0) ]
A2 = [ (0, -90, 0), (20, 90, 1), (10, 90, 1), (10, 45, 1), (14, 225, 1), (10, 0, 0), (10, 0, 0) ]
A3 = [ (0, -90, 0), (20, 90, 1), (10, 135, 1), (14, 225, 1), (10, 135, 1), (14, 225, 0), (20, 0, 0) ]
A4 = [ (0, -90, 0), (20, 180, 1), (10, -90, 1), (10, -90, 1), (10, 180, 1), (20, -90, 0),(10, 0, 0)]
A5 = [ (0, 0, 1), (10, -90, 1), (10, -90, 1), (10, 90, 1), (10, 90, 1), (10, 90, 0), (20, -90, 0), (10, 0, 0) ]
A6 = [ (0, -90, 1),  (10, 90, 1), (10, 90, 1), (10, 90, 1), (10, 90, 1), (10, 45, 1), (14, 135, 0), (20, -90, 0), (10, 0, 0)]
A7 = [ (0, -90, 0), (20, 90, 1), (10, 135, 1), (14, -45, 1), (10, -90, 0), (20, 0, 0)]
A8 = [ (0, 0, 1), (10, -90, 1), (20, -90, 1), (10, -90, 1), (20, -90, 0), (0, -90, 0), (10, 90, 1), (10, 90, 0), (10, -90,0), (10, 0, 0)]
A9 = [ (0,-45, 1), (14, -45, 1), (10, -90, 1), (10, -90, 1), (10, -90, 1), (10, 90, 0), (10, -90, 0), (10, 0, 0) ]

def f(A) :
    for step, angle, pen in A:
        t.forward(step)
        t.right(angle)
        if pen==0:
            t.penup()
        else:
            t.pendown()
f(A1)
f(A4)
f(A1)
f(A7)
f(A0)
f(A0)

