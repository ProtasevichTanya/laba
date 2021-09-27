import turtle as t

screen = t.Screen()
t.shape('circle')
t.speed(0)
t.penup()
x = -200
y = -200
t.goto(x,y)
t.pendown()
t.forward(10000)
t.left(180)
t.forward(10000)
t.left(180)
Vx = 20
Vy = 100
ay = -10
dt = 0.1
for _ in range(0,1000):
    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if y <= -200:
        y = -200
        Vy *= -0.8
        Vx *= 0.8
    if Vx < 1:
        ay = 0
        Vy = 0
    t.goto(x, y)
screen.exitonclick()
