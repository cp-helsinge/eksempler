import turtle
###################################################
# range = antal gange
# rigth or left = grader til højre eller venstre
# forward or backward = længde på streg + retning fremad/tilbage
# kan man tegne flere samtidig? hvordan
###################################################

for n in range(1,32):
    turtle.left(45)
    turtle.forward(n*7)

input()
