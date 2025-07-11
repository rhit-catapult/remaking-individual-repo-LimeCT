import sys

import pygame
import math
import random

# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed= random.randint(5, 25)
        self.radius= 50
        self.color= (154, 58, 212)
        self.speed_y = 5
        self.speed_x = 5


    def move(self):
        self.y += self.speed_y

    def bounce(self):
        self.x += self.speed_x
        self.y += self.speed_y


        if self.x - self.radius <= 0 or self.x + self.radius >= 1000:
            self.speed_x = -self.speed_x

        if self.y - self.radius <= 0 or self.y + self.radius >= 600:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(self.screen, (154, 58, 212), (self.x, self.y), 50, 3)

    def check_collision(self, Ball2):
        distance = math.sqrt((self.x - Ball2.x) ** 2 + (self.y - Ball2.y) ** 2)
        return distance <= self.radius + Ball2.radius

    def bounce_off(self, Ball2):
        if self.check_collision(Ball2):
            self.speed_x, Ball2.speed_x = -self.speed_x, -Ball2.speed_x
            self.speed_y, Ball2.speed_y = -self.speed_y, -Ball2.speed_y



def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Bouncing Ball')
    clock = pygame.time.Clock()

    # Create two Ball instances using the unified Ball class
    ball1 = Ball(screen, 320, 100)
    ball2 = Ball(screen, 550, 100)
    ball3 = Ball(screen, 430, 350)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(pygame.Color('gray'))

        # Move both balls
        ball1.move()
        ball2.move()
        ball3.move()

        # Check and respond to collisions between the two balls
        ball1.bounce_off(ball2)
        ball1.bounce_off(ball3)
        ball2.bounce_off(ball3)


        # Bounce off walls
        ball1.bounce()
        ball2.bounce()
        ball3.bounce()

        # Draw both balls
        ball1.draw()
        ball2.draw()
        ball3.draw()

        pygame.display.update()
        clock.tick(60)

main()