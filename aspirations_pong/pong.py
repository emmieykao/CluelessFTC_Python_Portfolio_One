"""
Description: plays ping pong
Author: Emmie Kao
Date: Fall 2021
"""

from graphics import *
import random
import math

#width and height of the window are both global constants
WIDTH = 600
HEIGHT = 400

#frames per second
FRAMES = 60

def createGraphicsWindow():
    """
    Inputs: none
    Outputs: a graphics window with a white background
    Purpose: draw a background/window
    """
    win = GraphWin('pong', WIDTH, HEIGHT)
    win.setBackground('Black')
    return win

def changeNumbers(win, right, left):
    leftPt = Point(WIDTH / 25, HEIGHT / 20)
    leftText = Text(leftPt, left)
    leftText.setFill('White')
    leftText.setSize(36)
    leftText.draw(win)

    rightPt = Point(WIDTH - (WIDTH / 25),HEIGHT / 20)
    rightText = Text(rightPt, right)
    rightText.setFill('White')
    rightText.setSize(36)
    rightText.draw(win)
    return leftText, rightText



def drawPaddles(win):
    left1 = Point(WIDTH - (WIDTH / 40), HEIGHT / 2 + HEIGHT / 10)
    left2 = Point(WIDTH, HEIGHT / 2 - HEIGHT / 10)
    leftPaddle = Rectangle(left1, left2)
    leftPaddle.setFill('White')
    leftPaddle.draw(win)
    right1 = Point(WIDTH / 40, HEIGHT / 2 + HEIGHT / 10)
    right2 = Point(0, HEIGHT / 2 - HEIGHT / 10)
    rightPaddle = Rectangle(right1, right2)
    rightPaddle.setFill('White')
    rightPaddle.draw(win)
    return rightPaddle, leftPaddle

def movePaddles(win, lPaddle, rPaddle):
        key = win.checkKey()
        if key == 'e':
            if lPaddle.getP2().getY() > 0:
                lPaddle.move(0, -HEIGHT / 16)
        elif key == 's':
            if lPaddle.getP1().getY() < HEIGHT:
                lPaddle.move(0, HEIGHT / 16)
        if key == 'Up':
            if rPaddle.getP2().getY() > 0:
                rPaddle.move(0, -HEIGHT / 16)
        elif key == 'Down':
            if rPaddle.getP1().getY() < HEIGHT:
                rPaddle.move(0, HEIGHT / 16)

def drawBall(win):
    p1 = Point(WIDTH / 2, 0)
    p2 = Point(WIDTH / 2, HEIGHT)
    center = Line(p1, p2)
    center.setWidth(2)
    center.setFill('White')
    center.draw(win)
    middle = Point(WIDTH / 2, HEIGHT / 2)
    ball = Circle(middle, HEIGHT / 100)
    ball.setFill('White')
    ball.setOutline('White')
    ball.draw(win)
    return ball

def playGame(win, lPaddle, rPaddle, ball):
    winner = False
    speed = max(WIDTH, HEIGHT) / 90
    velocity = [speed, speed]
    while not winner:
        while ball.getCenter().getX() < WIDTH + ball.getRadius() and \
        ball.getCenter().getX() > -ball.getRadius():
            ball.move(velocity[0], velocity[1])
            movePaddles(win, lPaddle, rPaddle)
            bounce(win, lPaddle, rPaddle, ball, velocity)
            time.sleep(1 / FRAMES * 1.2)
        winner = True
    return winner

def bounce(win, lPaddle, rPaddle, ball, speed):
    if ball.getCenter().getY() - ball.getRadius() + speed[1] < 0 or ball.getCenter().getY() + ball.getRadius() + speed[1] > HEIGHT:
        speed[1] *= -1
        ball.move(speed[0], speed[1])

    elif ball.getCenter().getX() - ball.getRadius() + speed[0] < WIDTH / 40 and \
    ball.getCenter().getY() - ball.getRadius() + speed[1] <= lPaddle.getP1().getY() and \
    ball.getCenter().getY() + ball.getRadius() + speed[1] >= lPaddle.getP2().getY():
        speed[0] = abs(speed[0])
        speed = randVector(speed)
        ball.move(speed[0], speed[1])


    elif ball.getCenter().getX() + ball.getRadius() + speed[1] > (WIDTH - (WIDTH / 40)) and \
    ball.getCenter().getY() - ball.getRadius() + speed[1] <= rPaddle.getP1().getY() and \
    ball.getCenter().getY() + ball.getRadius() + speed[1] >= rPaddle.getP2().getY():
        speed[0] = abs(speed[0])
        speed = randVector(speed)
        speed[0] *= -1
        ball.move(speed[0], speed[1])



def randVector(list):
    firstDiff = random.random()
    list[0] = list[0] + firstDiff
    secondDiff = random.random()
    list[1] = list[1] + secondDiff

    return list

def main():
    leftScore = 0
    rightScore = 0
    gw = createGraphicsWindow()
    while True:
        leftWritten, rightWritten = changeNumbers(gw, leftScore, rightScore)
        left, right = drawPaddles(gw)
        playBall = drawBall(gw)
        gameEnds = playGame(gw, left, right, playBall)
        if gameEnds == True:
            if playBall.getCenter().getX() < WIDTH / 2:
                leftScore += 1
            else:
                rightScore += 1

            right.undraw()
            left.undraw()

        time.sleep(1)
        leftWritten.undraw()
        rightWritten.undraw()


main()
