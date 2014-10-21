__author__ = 'WilsonKoder'

import pygame
import pygame.mixer
import random
import sys




white = 255, 255, 255

pygame.init()
pygame.mixer.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pong - Wilson Koder")


paddle1 = pygame.image.load("Images/paddle.png")
paddle2 = pygame.image.load("Images/paddle.png")
ball = pygame.image.load("Images/ball.png")
bg = pygame.image.load("Images/bg.png")

running = True
x1 = 5
y1 = 260
x2 = 780
y2 = 260
ball_pos = pygame.math.Vector2(385, 285)
ball_velocity = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))
paddle1_up = False
paddle1_down = False
paddle2_up = False
paddle2_down = False
clock = pygame.time.Clock()

while running:
    #FPS
    clock.tick(60)
    #move ball
    ball_pos += ball_velocity

    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_up = True
            if event.key == pygame.K_s:
                paddle1_down = True
            if event.key == pygame.K_UP:
                paddle2_up = True
            if event.key == pygame.K_DOWN:
                paddle2_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle1_up = False
            if event.key == pygame.K_s:
                paddle1_down = False
            if event.key == pygame.K_UP:
                paddle2_up = False
            if event.key == pygame.K_DOWN:
                paddle2_down = False

        if paddle1_up:
            y1 -= 10
        if paddle1_down:
            y1 += 10
        if paddle2_up:
            y2 -= 10
        if paddle2_down:
            y2 += 10


    #Audio
    if ball_pos[1] > window_size[1]:
        pygame.mixer.music.load("Audio/collision.wav")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        ball_velocity[1] = (ball_velocity[1] * -1)

    elif ball_pos[1] < 0:
        pygame.mixer.music.load("Audio/collision.wav")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        ball_velocity[1] = (ball_velocity[1] * -1)

    if ball_pos[0] > window_size[0]:
        pygame.mixer.music.load("Audio/endgame.wav")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()

    if ball_pos[0] < 0:
        pygame.mixer.music.load("Audio/endgame.wav")
        pygame.mixer.music.stop()
        pygame.mixer.music.play()


    #Collision Checking
    if int(ball_pos[0]) in range(0, 30) and int(ball_pos[1]) in range(y1 - 40, y1 + 40):
        ball_velocity = (ball_velocity * -1)
        ball_velocity[0] = random.randint(1, 11)
        ball_velocity[1] = random.randint(-10, 11)

    if int(ball_pos[0]) in range(777, 800) and int(ball_pos[1]) in range(y1 - 40, y1 + 40):
        ball_velocity = (ball_velocity * -1)
        ball_velocity[0] = random.randint(-1, -11)
        ball_velocity[1] = random.randint(-10, 11)

    #clear the screen
    screen.fill(white)

    #draw everything again
    screen.blit(bg, (0, 0))
    screen.blit(paddle1, (x1, y1))
    screen.blit(paddle2, (x2, y2))
    screen.blit(ball, ball_pos)

    #render it
    pygame.display.flip()

sys.exit()