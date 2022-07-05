import sys, random
import pygame
from pygame.locals import *
# ゲーム画面を初期化 --- (*1)
pygame.init()
screen = pygame.display.set_mode((600, 400))
white = (255,255,255)
black = (0,0,0)
# 繰り返し画面を描画 --- (*2)
while True:
    # 背景と円を描画 --- (*3)
    screen.fill(black) # 背景を黒で塗りつぶす
    pygame.draw.circle(screen, white, (300,200), 150) # 円を描画
    # 画面を更新 --- (*4)
    pygame.display.update()
    # 終了イベントを確認 --- (*5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()