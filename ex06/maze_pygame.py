import pygame as pg
import sys

class Screen:

    def __init__(self) -> None:
        
        pg.display.set_caption("こうかとん迷路")

        self.x = 16 # 迷路のxマス数
        self.y = 9 # 迷路のyマス数
        self.tile_length = 100 #タイルの大きさ

        self.sfc_screen = pg.display.set_mode((self.x*self.tile_length+14,self.y*self.tile_length+17))
        self.rct_sfc_screen = self.sfc_screen.get_rect()

        self.wall_color = (0,100,0)
        self.floor_color = (216,208,104)

        self.maze_map = [[rd.randint(0,1) for j in range(self.x)] for i in range(self.y)]

    def draw_map(self):
        self.sfc_screen.fill(self.floor_color)
        for i in range(self.y):
            for j in range(self.x):
                if self.maze_map[i][j] == 1:
                    pg.draw.rect(
                        self.sfc_screen,
                        color=self.wall_color,
                        rect=(j*(self.tile_length+1),i*(self.tile_length+1),(self.tile_length-1),(self.tile_length-1)),
                        width=0)