import turtle
import math

turtle.shape('turtle')
for i in range (3, 13, 1):
    a=360/i/2
    R=10+25*(i-2)
    b=R*2*math.sin(math.radians(a))
    turtle.penup()
    turtle.goto(R, 0)
    turtle.pendown()
    turtle.left(90+a)
    for j in range(i):
        turtle.forward(b)
        turtle.left(2*a)
    turtle.right(90+a)
    
    

