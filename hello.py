import turtle
#turtle.pencolor((120,255,20))
turtle.pencolor((0.5,1,0.08))
turtle.pensize(5)
for n in range(1,100000):
    print("n=", n)
    turtle.left(120)
    turtle.forward(n*20)

input()
