# Use modules
from mod1 import *
from mod2 import *
import turtle

turtle.speed(1000)
turtle.color(0.4,0,1)
turtle.pensize(4)

def move(x=0,y=0):
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()

def flower():
  for n in range(1,11):
    circle(50)
    turtle.left(36)

def weird_flower():
  for n in range(1,10):
    square(100)
    triangle(200)
    circle(50)
    turtle.left(36)

for n in range(-4,5):
  move(n*200,-300)
  flower()

for n in range(-2,3):
  move(n*350,200)
  weird_flower()

square()

input()