from asyncio import Event

import pygame, sys
def ball_collisions():
    global ball_speed_x,ball_speed_Y,screen_height,screen_width
    ball.x += ball_speed_x
    ball.y += ball_speed_Y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_Y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
        if ball.colliderect(player) or ball.colliderect(opponent):
         ball_speed_x *= -1

pygame.init()
lock = pygame.time.Clock()
screen_width = 1280
screen_height = 960
jello = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15, 30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7
ball_speed_Y = 7
player_speed = 0
opponent_speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            player_speed += 7
        if event.key == pygame.K_UP:
            player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed +=7
                if event.key == pygame.K_UP:
                    player_speed -= 7
    ball_collisions()
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
        if player.bottom >= screen_height:
            player_bottom = screen_height
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > screen_height:
        opponent.bottom -= opponent_speed
        if opponent.top <= 0:
            opponent.top = 0
            if opponent.bottom >= screen_height:
                player.bottom = screen_height


    jello.fill(bg_color)
    pygame.draw.rect(jello, light_grey, player)
    pygame.draw.rect(jello, light_grey, opponent)
    pygame.draw.ellipse(jello, light_grey, ball)
    pygame.draw.aaline(jello, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.display.flip()
    lock.tick(60)