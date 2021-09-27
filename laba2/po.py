import turtle as t

t.shape('turtle')
      
po=open('post.txt','r')
bigList=[]
a=-1
b=-1
for i in range(0,10):
    vString=po.readline()
    listdig=[]
    for j in range(len(vString)):
        if vString[j]=="(":
            a=int(j) 
        elif vString[j]==")":
            b=int(j)
        if a!=-1 and b!=-1:
            List=tuple(map(int, vString[a+1:b].split(",")))
            listdig.append(List)
            a=-1
            b=-1
    bigList.append(listdig)
po.close()

print(bigList[1])
def f(A) :
    for step, angle, pen in A:
        t.forward(step)
        t.right(angle)
        if pen==0:
            t.penup()
        else:
            t.pendown()
            
f(bigList[1])
f(bigList[4])
f(bigList[1])
f(bigList[7])
f(bigList[0])
f(bigList[0])

