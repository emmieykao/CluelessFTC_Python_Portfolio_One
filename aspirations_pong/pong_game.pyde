'''
Name: Emmie Kao
Date: September 5, 2023
Description: 2-Player Game for Pong. Left player uses 'w' and 's' keys; right player uses 'o' and 'l'
'''

from __future__ import print_function
from random import randrange

WIDTH = 500 #width of screen
HEIGHT = 500 #height of screen
PINGPONG = 3 #number of balls
PINGPONG_SIZE = 25 #ball diameter
PADDLE_WIDTH = 15
PADDLE_HEIGHT = HEIGHT / 5
PADDLE_SPEED = 25
objs = [] #global list for all objects
score_left = 0
score_right = 0

def setup():
    global objs
    size(WIDTH, HEIGHT)
    objs.append(Paddle(0, 2 * (HEIGHT / 5), PADDLE_SPEED, "w", "s"))
    objs.append(Paddle(WIDTH - PADDLE_WIDTH, 2 * (HEIGHT / 5), PADDLE_SPEED, "o", "l"))
    for i in range(PINGPONG):
        objs.append(Ball(WIDTH / 2,(i + 1) * (HEIGHT / (2 * PINGPONG)) + (HEIGHT / (2 * PINGPONG))))
    
def draw():
    global score
    background(0,0,0)
    stroke(255)
    fill(0,0,0)
    circle(WIDTH / 2, HEIGHT / 2, (WIDTH * HEIGHT) / 1000)
    line(WIDTH / 2,0,WIDTH / 2,HEIGHT)
    fill(255)
    
    text_size = ((WIDTH * HEIGHT) / 100000) * 36
    textSize(text_size)
    text(score_left, 1 * (WIDTH / 7), HEIGHT / 7)
    text(score_right, 5 * (WIDTH / 7), HEIGHT / 7)
    
    for obj in objs[0:2]:
        fill(255)
        rect(obj.x, obj.y, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    for obj in objs[2:]:
        fill(255)
        circle(obj.x, obj.y, PINGPONG_SIZE)
        
    for obj in objs[2:]:
        obj.x += obj.speed[0]
        obj.y += obj.speed[1]
        obj.bounce(objs[0], objs[1])
        obj.check()
    
class Ball():
    # class for each ping pong ball
    def __init__(self, x, y):
        #initializes the class
        self.x = x
        self.y = y
        self.speed = [randrange(WIDTH / -100,WIDTH / 100),randrange(HEIGHT / -100, HEIGHT / 100)]
        
    def bounce(self, paddle_left, paddle_right):
        #changes ball vector when it bounces off a surface
        
        if self.y - PINGPONG_SIZE / 2 <= 0 or self.y + PINGPONG_SIZE / 2 >= HEIGHT:
            self.speed[1] = self.speed[1] * -1
            self.speed[0] = self.speed[0] * (1 + randrange(0, 100) / 200)
            self.speed[1] = self.speed[1] * (1 + randrange(0, 100) / 200)
        
        if self.x - PINGPONG_SIZE / 2 <= paddle_left.x + PADDLE_WIDTH and self.y > paddle_left.y and self.y < paddle_left.y + PADDLE_HEIGHT:
            self.speed[0] = self.speed[0] * -1
            self.speed[0] = self.speed[0] * (1 + randrange(0, 100) / 200) + randrange(0, WIDTH / 400)
            self.speed[1] = self.speed[1] * (1 + randrange(0, 100) / 200) + randrange(0, WIDTH / 400)
        
        if self.x + PINGPONG_SIZE / 2 > paddle_right.x and self.y > paddle_right.y and self.y < paddle_right.y + PADDLE_HEIGHT:
            self.speed[0] = self.speed[0] * -1
            self.speed[0] = self.speed[0] * (1 + randrange(0, WIDTH / 5) / (WIDTH / 2)) + randrange(WIDTH / -400, 0)
            self.speed[1] = self.speed[1] * (1 + randrange(0, WIDTH / 5) / (WIDTH / 2)) + randrange(WIDTH / -400, 0)
    
    def check(self):
        # change the score if the ball passes a paddle
        global score_left
        global score_right
        global objs
        if self.x + PINGPONG_SIZE / 2 <= 0:
            score_right += 1
            objs.remove(self)
            
        if self.x - PINGPONG_SIZE / 2 >= WIDTH:
            score_left += 1
            objs.remove(self)
        
class Paddle():
    def __init__(self, x, y, speed, up, down):
        #initializes the class. these variables will be used in separate functions, so no other class functions.
        self.x = x
        self.y = y
        self.speed = speed
        self.up = up
        self.down = down 
                    
def keyPressed():
    #move the paddles up and down, unless they're at the edges of the screen
    if objs[0].y > 0:
        if key == objs[0].up:
            objs[0].y -= objs[0].speed
    if objs[0].y + PADDLE_HEIGHT < HEIGHT:
        if key == objs[0].down:
            objs[0].y += objs[0].speed

    if objs[1].y > 0:
        if key == objs[1].up:
            objs[1].y -= objs[1].speed
    if objs[1].y + PADDLE_HEIGHT < HEIGHT:
        if key == objs[1].down:
            objs[1].y += objs[1].speed
    
