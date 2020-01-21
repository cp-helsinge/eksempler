import turtle
# range = antal gange
# rigth or left = grader
# forward or backward = længde på streg + retning
# kan man tegne flere samtidig? hvordan

for n in range(1,100):
    turtle.left(45)
    turtle.forward(n*7)
    
input()