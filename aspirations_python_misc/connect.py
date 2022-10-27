"""
Purpose: to let the user draw a polygon on the screen
Author: Emmie Kao
Date: Fall 2021
"""
from time import sleep
import random

from graphics import *

#width and height of the window are both global constants
WIDTH = 600
HEIGHT = 400

def makeGraphicsWindow():
    """
    Inputs: none
    Outputs: a graphics window with a white background
    Purpose: draw a background/window
    """
    win = GraphWin('Connect the Dots', WIDTH, HEIGHT)
    win.setBackground('White')
    return win

def drawFirstGreyLine(win):
    """
    Inputs: window to draw in
    Outputs: none
    Purpose: to draw a grey line at the bottom
    """
    p1 = Point(0, HEIGHT)
    p2 = Point(WIDTH, HEIGHT)
    line = Line(p1, p2)
    line.setFill('Grey')
    line.setOutline('Grey')
    line.setWidth(HEIGHT / 2)
    line.draw(win)
    p3 = Point(WIDTH / 2, HEIGHT * (7/8))
    instructions = Text(p3, 'Click above to add dots, then click here to see \
shape')
    instructions.setSize(15)
    instructions.setTextColor('Black')
    instructions.draw(win)

def randomColor():
    """
    Inputs: none
    Outputs: red, blue, and green color coordinates
    Purpose: to create a random color
    """
    redVal = random.randrange(255)
    greenVal = random.randrange(255)
    blueVal = random.randrange(255)
    myColor = color_rgb(redVal, greenVal, blueVal)
    return myColor

def endInstructions(win):
    """
    Inputs: window to draw in
    Outputs: none
    Purpose: end the program with a user click
    """
    center = Point(WIDTH / 2, HEIGHT / 2)
    instructions = Text(center, 'Click anywhere to exit.')
    instructions.setSize(15)
    instructions.setTextColor('Black')
    instructions.draw(win)
    click = win.getMouse()

def main():
    gw = makeGraphicsWindow()
    drawFirstGreyLine(gw)
    isInGrey = False
    points = []
    while not isInGrey:
        point = gw.getMouse()
        if point.getY() > ((3 / 4) * HEIGHT):
            isInGrey = True
        else:
            point.draw(gw)
            points.append(point)
    polygon = Polygon(points)
    color = randomColor()
    polygon.setFill(color)
    polygon.draw(gw)
    endInstructions(gw)

main()
