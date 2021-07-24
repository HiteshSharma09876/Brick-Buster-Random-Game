

# Windows, MacOSX, and Linux Compatible
# Code by- Hitesh Sharma for Code in place
# Standford University ,2021
# BRICK BUSTER RANDOM 1.0
#

import pygame
import sys
import math
import random
import time



pygame.init()
pygame.display.set_caption("BRICK BUSTER RANDOM 1.0")
clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 800

AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
GREEN = (0, 128, 0)
LIME = (0, 255, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


# Creating the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create classes
class Paddle():
    def __init__(self):
        self.x = WIDTH / 2.0
        self.y = 700
        self.dx = 0
        self.width = 200
        self.height = 25
        self.score = 0

    def left(self):
        self.dx = -12

    def right(self):
        self.dx = 12

    def move(self):
        self.x = self.x + self.dx

        #border collision
        if self.x < 0 + self.width / 2.0:
            self.x = 0 + self.width / 2.0
            self.dx = 0

        elif self.x > WIDTH - self.width / 2.0:
            self.x = WIDTH - self.width / 2.0
            self.dx = 0

    def render(self):
        pygame.draw.rect(screen, YELLOW,
                         pygame.Rect(int(self.x - self.width / 2.0), int(self.y - self.height / 2.0), self.width,
                                     self.height))


class Ball():
    def __init__(self):
        self.x = WIDTH / 2.0
        self.y = HEIGHT / 2.0
        self.dx = 6
        self.dy = -6
        self.width = 20
        self.height = 20

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        # border collision
        if self.x < 0 + self.width / 2.0:
            self.x = 0 + self.width / 2.0
            self.dx *= -1

        elif self.x > WIDTH - self.width / 2.0:
            self.x = WIDTH - self.width / 2.0
            self.dx *= -1

        if self.y < 0 + self.height / 2.0:
            self.y = 0 + self.height / 2.0
            self.dy *= -1

        elif self.y > HEIGHT - self.height / 2.0:
            self.y = HEIGHT - self.height / 2.0
            self.x = WIDTH / 2.0
            self.y = HEIGHT / 2.0

    def render(self):
        pygame.draw.rect(screen, WHITE,
                         pygame.Rect(int(self.x - self.width / 2.0), int(self.y - self.height / 2.0), self.width,
                                     self.height))

    def is_object_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)






class Brick():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 25
        self.color = random.choice([WHITE, GREEN, RED, BLUE,FUCHSIA,GRAY ,GREEN,LIME,MAROON, NAVYBLUE,OLIVE ,
                                    RED ,SILVER ,TEAL,YELLOW])

    def render(self):
        pygame.draw.rect(screen, self.color,
                         pygame.Rect(int(self.x - self.width / 2.0), int(self.y - self.height / 2.0), self.width,
                                     self.height))



#creating font
font = pygame.font.SysFont("georgia", 48)


# Creating game objects
paddle = Paddle()
ball = Ball()

bricks = []
for y in range(150, 375, 25):
    color = random.choice([WHITE, GREEN, RED, BLUE,FUCHSIA,GRAY ,GREEN,LIME,MAROON, NAVYBLUE,OLIVE ,
                                    RED ,SILVER ,TEAL])
    for x in range(150, 1100, 50):
        bricks.append(Brick(x, y))
        bricks[-1].color = color

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time.sleep(3)
            sys.exit()

        # Keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.left()
            elif event.key == pygame.K_RIGHT:
                paddle.right()

    # Updating objects
    paddle.move()
    ball.move()

    # Checking  collisions
    if ball.is_object_collision(paddle):
        ball.dy *= -1


    dead_bricks = []
    for brick in bricks:
        if ball.is_object_collision(brick):
            ball.dy *= -1
            dead_bricks.append(brick)
            paddle.score += 10


    for brick in dead_bricks:
        bricks.remove(brick)


    if len(bricks) == 0:

            pygame.init()

            # creating display
            display = pygame.display.set_mode((1000, 1500))

            # Creating the image surface
            image = pygame.image.load('thankyou.png')

            # puting our image surface on display surface
            display.blit(image, (200, 50))



            # creating a running loop
            while True:

                # creating a loop to cheack events that are occuring
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                # updating the display
                pygame.display.flip()


    # background colour
    screen.fill(BLACK)

    # Render objects
    paddle.render()
    ball.render()

    for brick in bricks:
        brick.render()

    # Render the time


    score_surface = font.render(f" COMPLETE WITHIN 3 mins \n Player Score: {paddle.score}", True, WHITE)
    screen.blit(score_surface, (WIDTH / 2.0 - 600, 20))
    pygame.display.flip()

    clock.tick(30)
