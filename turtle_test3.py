import turtle
###################################################
# range = antal gange
# rigth or left = grader til højre eller venstre
# forward or backward = længde på streg + retning fremad/tilbage
# kan man tegne flere samtidig? hvordan
###################################################

for n in range(1,100):
    turtle.left(90)
    turtle.forward(n*3)
    
    
input()