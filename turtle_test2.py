import turtle
# range = antal gange
# rigth or left = grader
# forward or backward = længde på streg + retning
# kan man tegne flere samtidig? hvordan

for n in range(1,10):
    turtle.left(90)
    turtle.forward(n*2)
    turtle.left(90)
    turtle.forward(n*10)
    turtle.right(90)
    turtle.forward(n*2)
    turtle.right(90)
    turtle.forward(n*10)
for n in range(1,40):
    turtle.left(90)
    turtle.forward(n*10)

