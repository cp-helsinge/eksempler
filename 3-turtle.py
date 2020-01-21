# Brug af turtle
import turtle

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(135)
turtle.forward(141)
turtle.left(45)
turtle.forward(100)

input()

# Color and size
# turtle.pencolor((0.5,0,1))
# turtle.pensize(5)

# the power of for loops
for n in range(1,32):
    turtle.left(90)
    turtle.forward(n*20)

input()

