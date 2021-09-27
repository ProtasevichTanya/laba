import turtle
from random import *

turtle.shape('turtle')
turtle.speed(0)
turtle.color('purple')
for i in range (500):
    turtle.forward(randint(0, 100))
    turtle.left(randint(0, 360))
