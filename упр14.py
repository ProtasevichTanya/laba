import turtle

turtle.shape('turtle')
a=5
x=180/a
b=11
y=180/b
for i in range (a):
    turtle.right(180-x)
    turtle.forward(100)

turtle.penup()
turtle.goto( 150, 0)
turtle.pendown()
    
for i in range (b):
    turtle.right(180-y)
    turtle.forward(100)
