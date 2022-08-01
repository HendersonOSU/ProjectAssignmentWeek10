from turtle import Turtle
import math
import sys
import time


def drawKochFractal(width, height, size, level):

 
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(-width // 3, height // 4)
    t.down()

    drawFractalLine(t, size, 0, level);
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)

def drawFractalLine(t, distance, theta, level):



    if (level == 0):
        drawPolarLine(t, distance, theta)
    else:
        drawFractalLine(t, distance//3, theta, level - 1)
        drawFractalLine(t, distance//3, theta + 60, level - 1)
        drawFractalLine(t, distance//3, theta - 60, level - 1)
        drawFractalLine(t, distance//3, theta, level - 1)

# drawPolarLine function
def drawPolarLine(t, distance, theta):


    t.setheading(theta)
    t.forward(distance)

def main():

    level = int(input("Enter a level: "))
    time.sleep(2)
    print("Let it snow!!!")
    time.sleep(2)

    drawKochFractal(200, 200, 150, level)

main()
