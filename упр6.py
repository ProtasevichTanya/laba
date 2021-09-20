import turtle

print('Введите число лап')
n=int(input())
a=360/n
turtle.shape('turtle')
b=0
while b<n:
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.goto(0, 0)
    turtle.left(180-a)
    b+=1




