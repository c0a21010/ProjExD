# %%
import pygame as pg
import sys
import random as rd

# %%
class Screen:

    def __init__(self) -> None:
        
        pg.display.set_caption("こうかとん迷路")

        self.x = 16 # 迷路のxマス数
        self.y = 9 # 迷路のyマス数
        self.tile_length = 100 #タイルの大きさ

        self.sfc = pg.display.set_mode((self.x*self.tile_length+14,self.y*self.tile_length+17))
        self.rct = self.sfc.get_rect()

        self.start_color = (0,0,255)

        self.wall_color = (0,100,0)
        self.floor_color = (216,208,104)

        self.goal_color = (255,0,0)

        """ self.maze_map = [[rd.randint(0,1) for j in range(self.x)] for i in range(self.y)] """
        self.maze_map = self.make_maze(self.x,self.y)

    def draw_map(self):
        self.sfc.fill(self.floor_color)
        for i in range(self.y):
            for j in range(self.x):
                if self.maze_map[i][j] == 1:
                    color = self.wall_color
                    """ if i==1 and j==1 : color = self.start_color
                    elif i==self.y-2 and j==self.x-2: color = self.goal_color
                    print(color) """
                    pg.draw.rect(
                        surface=self.sfc,
                        color=color,
                        rect=(j*(self.tile_length+1),i*(self.tile_length+1),(self.tile_length-1),(self.tile_length-1)),
                        width=0)
                    pg.draw.rect(
                        surface=self.sfc,
                        color=self.start_color,
                        rect=(1*(self.tile_length+1),1*(self.tile_length+1),(self.tile_length-1),(self.tile_length-1)),
                        width=0)
                    pg.draw.rect(
                        surface=self.sfc,
                        color=self.goal_color,
                        rect=((self.x-2)*(self.tile_length+1),(self.y-2)*(self.tile_length+1),(self.tile_length-1),(self.tile_length-1)),
                        width=0)

    def make_maze(self,yoko, tate):
        XP = [ 0, 1, 0, -1]
        YP = [-1, 0, 1,  0]

        maze_lst = []
        for y in range(tate):
            maze_lst.append([0]*yoko)
        for x in range(yoko):
            maze_lst[0][x] = 1
            maze_lst[tate-1][x] = 1
        for y in range(1, tate-1):
            maze_lst[y][0] = 1
            maze_lst[y][yoko-1] = 1
        for y in range(2, tate-2, 2):
            for x in range(2, yoko-2, 2):
                maze_lst[y][x] = 1
        for y in range(2, tate-2, 2):
            for x in range(2, yoko-2, 2):
                if x > 2: rnd = rd.randint(0, 2)
                else:     rnd = rd.randint(0, 3)
                maze_lst[y+YP[rnd]][x+XP[rnd]] = 1

        return maze_lst

    def reset_maze(self):
        self.maze_map = self.make_maze(self.x,self.y)

# %%
def make_maze(yoko, tate):
    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]

    maze_lst = []
    for y in range(tate):
        maze_lst.append([0]*yoko)
    for x in range(yoko):
        maze_lst[0][x] = 1
        maze_lst[tate-1][x] = 1
    for y in range(1, tate-1):
        maze_lst[y][0] = 1
        maze_lst[y][yoko-1] = 1
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            maze_lst[y][x] = 1
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            if x > 2: rnd = rd.randint(0, 2)
            else:     rnd = rd.randint(0, 3)
            maze_lst[y+YP[rnd]][x+XP[rnd]] = 1

    return maze_lst

def show_maze(canvas, maze_lst):
    color = ["white", "gray"]
    for y in range(len(maze_lst)):
        for x in range(len(maze_lst[y])):
            canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, 
                                    fill=color[maze_lst[y][x]])

# %%
class Bird:
    def __init__(self, image, size, scr):
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rct = self.sfc.get_rect()
        self.size = size

        self.scr = scr
        self.tile_size = self.scr.tile_length

        self.xy = 1+1j
        self.rct.center = (int(self.xy.real)*self.tile_size+(self.rct.size[0]//2),int(self.xy.imag)*self.tile_size+(self.rct.size[1]//2))

    """ def check_bound(self,rct, scr_rct):
        yoko, tate = +1, +1  # 領域内
        if rct.left < scr_rct.left or scr_rct.right < rct.right:
            yoko = -1  # 領域外
        if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
            tate = -1  # 領域外
        return yoko, tate """

    def update(self, scr):

        tmp = self.xy
        key_states = pg.key.get_pressed()  # 辞書
        if key_states[pg.K_UP]:
            """ self.rct.centery -= 1 """
            self.xy -= 1j
        if key_states[pg.K_DOWN]:
            """ self.rct.centery += 1 """
            self.xy += 1j
        if key_states[pg.K_LEFT]:
            """ self.rct.centerx -= 1 """
            self.xy -= 1
        if key_states[pg.K_RIGHT]:
            """ self.rct.centerx += 1 """
            self.xy += 1

        if scr.maze_map[int(self.xy.imag)][int(self.xy.real)] != 1:
            self.rct.center = (int(self.xy.real)*self.tile_size+(self.rct.size[0]//2),int(self.xy.imag)*self.tile_size+(self.rct.size[1]//2))
        else:
            self.xy = tmp

        if self.xy == complex(self.scr.x-2,self.scr.y-2):
            self.scr.reset_maze()
            self.xy = 1+1j
            self.rct.center = (int(self.xy.real)*self.tile_size+(self.rct.size[0]//2),int(self.xy.imag)*self.tile_size+(self.rct.size[1]//2))
        # 練習7
        """ if self.check_bound(self.rct, scr.rct) != (1, 1):  # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1 """
        scr.sfc.blit(self.sfc,self.rct)

# %%
from random import randint


class Bear(Bird):
    def __init__(self, image, size, scr):
        super().__init__(image, size, scr)
        self.xy = complex(self.scr.x-2,self.scr.y-2)
        self.rct.center = (int(self.xy.real)*self.tile_size+(self.rct.size[0]//2),int(self.xy.imag)*self.tile_size+(self.rct.size[1]//2))
    def update(self, scr):
        tmp = self.xy
        # クマの行動
        if rd.randint(0,1) == True:
            self.xy += complex(rd.randint(-1,1),0)
        else:
            self.xy += complex(0,rd.randint(-1,1))
        # 以下は同様
        if scr.maze_map[int(self.xy.imag)][int(self.xy.real)] != 1:
            self.rct.center = (int(self.xy.real)*self.tile_size+(self.rct.size[0]//2),int(self.xy.imag)*self.tile_size+(self.rct.size[1]//2))
        else:
            self.xy = tmp
        # 練習7
        """ if self.check_bound(self.rct, scr.rct) != (1, 1):  # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1 """
        scr.sfc.blit(self.sfc,self.rct)

# %%
def main():
    running = True
    scr = Screen()
    kkt = Bird("fig/6.png", 2.0,scr)
    brs = [Bear("animal_kowai_kuma.png",0.125,scr) for i in range(3)]
    clock = pg.time.Clock()

    counter = 0


    while running:
        # ここにコードを書く
        if counter > 100:
            brs.append(Bear("animal_kowai_kuma.png",0.125,scr))
            counter = 0

        scr.draw_map()
        kkt.update(scr)
        """ brs[0].update(scr) """
        for b in brs:
            b.update(scr)

        for b in brs:
            if kkt.rct.colliderect(b.rct):
                pg.quit()
                sys.exit()


        # イベント処理部
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 終了イベント
                running = False
                pg.quit()  #pygameのウィンドウを閉じる
                sys.exit() #システム終了            

        pg.display.update() #描画処理を実行
        counter += 1
        clock.tick(10)

# %%
if __name__ == '__main__':
    main()


