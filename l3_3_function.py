import turtle

turtle.speed(3)

def square(size):
    for n in range(4):
        turtle.forward(size)
        turtle.left(90)

for n in range(10):
    square(100)
    turtle.left(36)

turtle.exitonclick()

