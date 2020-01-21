import turtle
# range = antal gange
# rigth or left = grader
# forward or backward = længde på streg + retning
# kan man tegne flere samtidig? hvordan

for n in range(1,80):
    turtle.left(80)
    turtle.forward(n*2)
    turtle.right(40)
    turtle.backward(n*2)
for n in range(1,50):
    turtle.right(80)
    turtle.forward(n*1.5)
    
    input()