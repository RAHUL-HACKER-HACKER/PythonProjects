#question  10  ans--------------------------

def function(parameter):
    str=parameter
    return str

fn=function("hello i am function")
print(fn)






#question 11 ans-----------------------

import pygame

import math

import sys

pygame.init()



screen = pygame.display.set_mode((600, 300)) 

#setting caption

pygame.display.set_caption("Elliptical orbit")

#creating clock variable

clock=pygame.time.Clock() 

while(True):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

# setting x and y radius of ellipse    

    xRadius = 250

    yRadius = 100

    for degree in range(0,360,10):

        x1 = int(math.cos(degree * 2 * math.pi/360) * xRadius)+300

        y1 = int(math.sin(degree * 2 * math.pi/360) * yRadius)+150

        screen.fill((0, 0, 0))

        pygame.draw.circle(screen, (255, 69, 0), [300, 150], 40)

        pygame.draw.ellipse(screen,(255,255,255),[50,50,500,200],1)

        pygame.draw.circle(screen, (0, 255, 0), [x1, y1], 20)






#question  12 ans---------------------------

import sys, pygame

pygame.init()

size = width, height = 800, 400

speed = [1, 1]

background = 255, 255, 255

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing ball")

ball = pygame.image.load("ball.png")

ballrect = ball.get_rect()

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:

        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:

        speed[1] = -speed[1]

    screen.fill(background)

    screen.blit(ball, ballrect)

    pygame.display.flip()