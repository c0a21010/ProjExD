import pygame as pg
import sys


def main():

    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    bg_img = pg.image.load(
        "/home/koya/MEGA/講義資料/2_前期/プロジェクト演習/3クール/ProjExD/ex04/pg_bg.jpg"
    )
    bg_rect = bg_img.get_rect()

    kokaton_img = pg.image.load(
        "/home/koya/MEGA/講義資料/2_前期/プロジェクト演習/3クール/ProjExD/ex04/6.png"
    )
    kokaton_img = pg.transform.rotozoom(kokaton_img, 0, 2.0)

    kokaton_rect = kokaton_img.get_rect()
    kokaton_rect.center = 900, 400

    while True:
        screen.blit(bg_img, bg_rect)
        screen.blit(kokaton_img, kokaton_rect)

        pg.display.update()

        clock.tick(1000)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
