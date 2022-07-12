import random
import sys

import pygame as pg


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)  # Surface
        self.rct = self.sfc.get_rect()  # Rect
        self.bgimg_sfc = pg.image.load(image)  # Surface
        self.bgimg_rct = self.bgimg_sfc.get_rect()  # Rect
        self.sfc.blit(self.bgimg_sfc, self.bgimg_rct)

        self.width = self.rct.width
        self.height = self.rct.height

    def blit(self):
        self.sfc.blit(self.bgimg_sfc, self.bgimg_rct)


class Bird:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.size = size

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        key_states = pg.key.get_pressed()  # 辞書
        if key_states[pg.K_UP] == True:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN] == True:
            self.rct.centery += 1
        if key_states[pg.K_LEFT] == True:
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True:
            self.rct.centerx += 1
        if key_states[pg.K_SPACE] == True:  # スペースキーを押したときに
            self.shield(scr)  # シールドを出す
            self.shield_flag = True  # フラグを使ってダメージがあるかを判定

        else:
            self.shield_flag = False
        if key_states[pg.K_b] == True:
            self.beam(scr)
        else:
            pass
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1):  # 領域外だったら
            if key_states[pg.K_UP] == True:
                self.rct.centery += 1
            if key_states[pg.K_DOWN] == True:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT] == True:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT] == True:
                self.rct.centerx -= 1
        self.blit(scr)

    def shield(self, scr):  # 円を出現させたりしている

        self.sld_sfc = pg.Surface((self.size * 100, self.size * 100))
        self.sld_rct = self.sld_sfc.get_rect()
        self.sld_rct.center = self.rct.center
        pg.draw.circle(
            self.sld_sfc,
            (0, 0, 255),
            (self.size * 50, self.size * 50),
            self.size * 50,
        )
        self.sld_sfc.set_colorkey((0, 0, 0))
        scr.sfc.blit(self.sld_sfc, self.sld_rct)
        # print(self.rct.center)


def check_bound(rct, scr_rct):
    yoko, tate = +1, +1  # 領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right:
        yoko = -1  # 領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
        tate = -1  # 領域外
    return yoko, tate


class Bomb:
    def __init__(self, color, hankei, vxy, scr):
        self.sfc = pg.Surface((2 * hankei, 2 * hankei))  # Surface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (hankei, hankei), hankei)
        self.rct = self.sfc.get_rect()  # Rect
        self.rct.centerx = random.randint(0, scr.width)
        self.rct.centery = random.randint(0, scr.height)
        self.vx, self.vy = +1, +1  # 練習6

    def update(self, scr):
        self.rct.move_ip(self.vx, self.vy)
        self.blit(scr)

        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


def main():
    clock = pg.time.Clock()
    scr = Screen("逃げろこうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    # bomb = Bomb((255, 0, 0), 10, (1, 1), scr)

    bomblist = []
    for i in range(2):
        bomblist.append(Bomb((255, 0, 0), 10, (1, 1), scr))

    # print(bomblist)

    count = 0

    while True:
        # print(len(bomblist))
        if count > 1000:
            count = 0
            bomblist.append(Bomb((255, 0, 0), 10, (1, 1), scr))

        scr.blit()
        kkt.update(scr)
        # bomb.update(scr)

        # print(kkt.shield_flag)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        for v in bomblist:
            v.update(scr)
            if kkt.rct.colliderect(v.rct) and not (kkt.shield_flag):
                return

        count += 1

        # if kkt.rct.colliderect(bomb.rct):
        #     return

        pg.display.update()
        clock.tick(150)


"""
def main():

    clock = pg.time.Clock()

    # 練習1：スクリーンと背景画像
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))  # Surface
    screen_rct = screen_sfc.get_rect()  # Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")  # Surface
    bgimg_rct = bgimg_sfc.get_rect()  # Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    # 練習3：こうかとん
    kkimg_sfc = pg.image.load("fig/6.png")  # Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)  # Surface
    kkimg_rct = kkimg_sfc.get_rect()  # Rect
    kkimg_rct.center = 900, 400

    # 練習5：爆弾
    bmimg_sfc = pg.Surface((20, 20))  # Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_rct = bmimg_sfc.get_rect()  # Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    vx, vy = +1, +1  # 練習6

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習4
        key_states = pg.key.get_pressed()  # 辞書
        if key_states[pg.K_UP] == True:
            kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] == True:
            kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] == True:
            kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True:
            kkimg_rct.centerx += 1
        # 練習7
        if check_bound(kkimg_rct, screen_rct) != (1, 1):  # 領域外だったら
            if key_states[pg.K_UP] == True:
                kkimg_rct.centery += 1
            if key_states[pg.K_DOWN] == True:
                kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT] == True:
                kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True:
                kkimg_rct.centerx -= 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        # 練習6
        bmimg_rct.move_ip(vx, vy)
        # 練習5
        screen_sfc.blit(bmimg_sfc, bmimg_rct)
        # 練習7
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        # 練習8
        if kkimg_rct.colliderect(bmimg_rct):
            return


        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):

   [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect

    yoko, tate = +1, +1  # 領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right:
        yoko = -1  # 領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
        tate = -1  # 領域外
    return yoko, tate

""" """"""


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
