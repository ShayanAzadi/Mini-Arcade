import pygame
from pong import pong
from snake import snake
from sumo import sumo
from target_destroyer import target_destroyer
from cards import cards
from flappy_shiit import flappy_shiit
from red_hands import red_hands
from race import race
from mench import mench
from wrestling import wrestling
from brick_hit import brick_hit
from space_cleaner import space_cleaner


pygame.init()

win = pygame.display.set_mode((600, 400))
run = True

ic = pygame.image.load("ic.png")
pygame.display.set_icon(ic)
pygame.display.set_caption("6")
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
img = []
for i in range(1, 13):
    img.append(pygame.transform.scale(pygame.image.load("icon/" + str(i) + ".png"), (200, 100)))
xy = []

y = 0
for i in range(4):
    x = 0
    for j in range(3):
        xy.append((x, y))
        x += 200
    y += 100

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            xm, ym = event.pos
            if 0 < xm < 200 and 0 < ym < 100:
                pong()
                win = pygame.display.set_mode((600, 400))
            if 200 < xm < 400 and 0 < ym < 100:
                snake()
                win = pygame.display.set_mode((600, 400))
            if 400 < xm < 600 and 0 < ym < 100:
                sumo()
                win = pygame.display.set_mode((600, 400))
            if 0 < xm < 200 and 100 < ym < 200:
                target_destroyer()
                win = pygame.display.set_mode((600, 400))
            if 200 < xm < 400 and 100 < ym < 200:
                cards()
                win = pygame.display.set_mode((600, 400))
            if 400 < xm < 600 and 100 < ym < 200:
                flappy_shiit()
                win = pygame.display.set_mode((600, 400))
            if 0 < xm < 200 and 200 < ym < 300:
                red_hands()
                win = pygame.display.set_mode((600, 400))
            if 200 < xm < 400 and 200 < ym < 300:
                mench()
                win = pygame.display.set_mode((600, 400))
            if 400 < xm < 600 and 200 < ym < 300:
                race()
                win = pygame.display.set_mode((600, 400))
            if 0 < xm < 200 and 300 < ym < 400:
                space_cleaner()
                win = pygame.display.set_mode((600, 400))
            if 200 < xm < 400 and 300 < ym < 400:
                wrestling()
                win = pygame.display.set_mode((600, 400))

            if 400 < xm < 600 and 300 < ym < 400:
                brick_hit()
                win = pygame.display.set_mode((600, 400))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.stop()


    pygame.display.set_icon(ic)
    pygame.display.set_caption("6")
    win.fill((200, 200, 200))
    for i in range(len(img)):
        win.blit(img[i], xy[i])
    pygame.display.update()

pygame.quit()
