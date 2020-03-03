import turtle
# Color and size
# turtle.pencolor((0.5,0,1))
# turtle.pensize(5)
turtle.speed('fast')
# the power of for loops
for n in range(1,32):
    turtle.left(15)
    turtle.forward(n*12)
    turtle.left(5)
    turtle.forward(n*3)

input()
