import turtle
from l4_3_func_file import square

turtle.speed(0)

for n in range(10):
    square(100)
    turtle.left(36)

turtle.exitonclick()