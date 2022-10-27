"""
Definition: uses graphics as a visual for selection sort
Author: Emmie Kao
Date: Winter 2022
"""
from graphics import *
import random
from time import sleep

WIDTH = 500
HEIGHT = 500

def createGraphWin() -> GraphWin:
    """
    Inputs: None
    Outputs: a blank graphics window
    Purpose: to create a blank graphics window
    """
    win = GraphWin('Selection Sort', WIDTH, HEIGHT)
    win.setBackground('white')
    return win

def drawBars(win: GraphWin) -> list:
    """
    Inputs: a graphics window to draw rectangles on
    Outputs: a list containing all of the rectangles
    Purpose: to draw a random amount of rectangles in a random order
    """
    barList = []
    amountBars = random.randrange(round(WIDTH / 20), round(WIDTH / 15))
    for i in range(amountBars):
        height = random.randrange(round(HEIGHT / 10), HEIGHT)
        p1 = Point((WIDTH / amountBars) * i, HEIGHT - height)
        p2 = Point((WIDTH / amountBars) * (i + 1), HEIGHT)
        bar = Rectangle(p1, p2)
        bar.setOutline('black')
        bar.setFill('red')
        bar.draw(win)
        barList.append(bar)
    return barList

def sortBars(win: GraphWin, barList: list) -> None:
    """
    Inputs: a window to draw in, the amount of rectangles to sort, and a list
    of the rectangles to sort.
    Outputs: none, but draws in window
    Purpose: to sort a group of rectangles using selection sort
    """
    for i, bar in enumerate(barList):
        #record the y value of the starting bar and color it yellow
        smallestBar = bar.getP1().getY()
        smallestBarLoc = i
        bar.setFill('yellow')
        #for every other bar in the set, color it blue, and if it is smaller
        #than the current smallest y-value, then it is the new smallest and
        #turns green.
        for j in range(i + 1, len(barList)):
            barList[j].setFill("cyan")
            currentY = barList[j].getP1().getY()
            time.sleep(0.05)
            if currentY > smallestBar:
                smallestBar = barList[j].getP1().getY()
                smallestBarLoc = j
                barList[smallestBarLoc].setFill('lime')
            #make sure all of the bars except the current smallest, starting,
            #and currently being read bars are red
            for k, rect in enumerate(barList):
                if k != smallestBarLoc and k > i:
                    rect.setFill("red")
        #turn the original bar red again; the smallest bar stays green
        bar.setFill("lime")
        barList[smallestBarLoc].setFill('red')
        #switch the smallest bar and the starting bar in the list; now, they
        #will be drawn at different times
        checkmarkPoint = barList[smallestBarLoc].getP1().getX()
        checkmarkPoint2 = bar.getP1().getX()
        bar.move(checkmarkPoint - checkmarkPoint2, 0)
        barList[smallestBarLoc].move(checkmarkPoint2 - checkmarkPoint, 0)
        #switch them in the original list as well
        barList[i], barList[smallestBarLoc] = barList[smallestBarLoc], \
barList[i]
    for bar in barList:
        bar.setFill('lime')
    textP1 = Point(WIDTH / 2, HEIGHT / 2)
    done = Text(textP1, 'DONE!')
    done.setFace('times roman')
    if round((HEIGHT * WIDTH) / 100) > 36:
        size = 36
    elif round((HEIGHT * WIDTH) / 100) < 5:
        size = 5
    else:
        size = round((HEIGHT * WIDTH) / 100)
    done.setSize(size)
    done.setStyle('bold')
    done.setFill('black')
    done.setOutline('black')
    done.draw(win)

def main():
    gw = createGraphWin()
    bars = drawBars(gw)
    sortBars(gw, bars)
    time.sleep(5)
main()
