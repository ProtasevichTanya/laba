import turtle as t

t.shape('turtle')
t.color('blue')
t.width(3)
t.penup()

A0 = [ (10, 90), (20, 90), (10, 90), (20, 90) ]
def f0() :
    t.pendown()
    for step, angle in A0:
        t.forward(step)
        t.left(angle)
    t.penup()
    t.forward(20)

A1 = [ (0, 270, 0), (10, 45, 1),(14, 135, 1), (20, 0, 0) ]
def f1() :
    for step, angle, pen in A1:
        t.forward(step)
        t.right(angle)
        if pen==0:
            t.penup()
        else:
            t.pendown()
    t.left(90)
    t.forward(10)

A2 = [ (0, 270,0), (20, 90, 1), (10, 90, 1), (10, 45, 1), (14, 225, 1), (10, 0, 0) ]
def f2():
    for step, angle, pen in A2:
        t.forward(step)
        t.right(angle)
        if pen==0:
            t.penup()
        else:
            t.pendown()
    t.forward(10)

A4 = [ (0, 270,0), (20, 180, 1), (10, 270, 1), (10, 270, 1), (10, 180, 1), (20, 270, 0),(10, 0, 0)]
def f4() :
    for step, angle, pen in A4:
        t.forward(step)
        t.right(angle)
        if pen==0:
            t.penup()
        else:
            t.pendown()
            
A7 = [ (0, 270,0), (20, 90, 1), (10, 135, 1), (14, 315, 1), (10, 270, 0), (20, 0, 0)]
def f7() :
    for step, angle, pen in A7:
        t.forward(step)
        t.right(angle)
        if pen==0:
            t.penup()
        else:
            t.pendown()


f1()
f4()
f1()
f7()
f0()
f0()
