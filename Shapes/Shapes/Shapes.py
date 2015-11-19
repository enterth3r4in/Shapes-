#Shapes
import math
import turtle

def bobMakesARay(turtle, size):
    for iter in range(2):
        drawArcr(bob,size,90)
        drawArcl(bob,size,90)

def bobMakesASun(turtle, size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for iter in range(2):
        bobMakesARay(turtle,size)
        turtle.right(160)
    turtle.end_fill()

def main():
    bob = turtle.Turtle()
    turtle.title('Sun Figure')
    turtle.setup(800, 800, 0, 0)

    bobMakesARay(bob, 50)

main()