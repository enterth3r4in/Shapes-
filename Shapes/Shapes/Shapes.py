#Shapes. In which Bob the turtle draws shapes.
import math
import turtle

def bobArcsRight(turtle, size, degrees):
    for iter in range(degrees):
        turtle.forward(size)
        turtle.right(1)

def bobArcsLeft(turtle, size, degrees):
    for iter in range(degrees):
        turtle.forward(size)
        turtle.left(1)

def bobMakesARay(turtle, size):
    for iter in range(2):
        bobArcsRight(turtle,size,90)
        bobArcsLeft(turtle,size,90)

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
    bob.speed(0)
    bobMakesASun(bob, 1, 'purple')
    turtle.done()

main()