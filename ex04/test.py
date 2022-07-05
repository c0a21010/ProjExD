import pygame as pg
import sys


def main():
    # pass

    clock = pg.time.Clock()
    pg.display.set_caption("初めてのPygame")
    screen = pg.display.set_mode((800, 600))

    tori_img = pg.image.load("6.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400
    screen.blit(tori_img, tori_rect)

    image = pg.Surface((100, 100))

    pg.draw.circle(image, (0, 0, 0), (50, 50), 10)

    clock.tick(0.2)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
