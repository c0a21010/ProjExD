# %%
import pygame as pg
import sys
import random as rd
import maze_maker

kuma_dia=0.125 #くまの倍率
tori_dia=1.5 #鳥の倍率

# %%
class Screen:

    def __init__(self, x_size, y_size) -> None:
        
        pg.display.set_caption("こうかとん迷路")

        self.x = x_size# 迷路のxマス数
        self.y = y_size# 迷路のyマス数
        self.tile_length = 100 #タイルの大きさ

        self.sfc = pg.display.set_mode((self.x*self.tile_length+14,self.y*self.tile_length+17))
        self.rct = self.sfc.get_rect()

        self.start_color = (0,0,255)

        self.wall_color = (0,100,0)
        self.floor_color = (216,208,104)

        self.goal_color = (255,0,0)
        
        self.maze_map = maze_maker.make_maze(self.x,self.y)
        self.goal_pos = self.goal_p() #ゴール座標をランダム設定

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
        #print(self.goal_pos[0]*self.tile_length+1)
        pg.draw.rect(
            surface=self.sfc,
            color=self.goal_color,
            rect=((self.goal_pos[0])*(self.tile_length+1),(self.goal_pos[1])*(self.tile_length+1),(self.tile_length-1),(self.tile_length-1)),
            width=0)
    
    def goal_p(self):
        height = len(self.maze_map) #高さを取得
        end_p=[] #ゴール候補のy座標のリスト
        for i in range(0, height):
            if not self.maze_map[i][-2]: #そのマスが床なら
                if self.maze_map[i][-3] + self.maze_map[i-1][-2] + self.maze_map[i+1][-2] == 2: #かつ、右側を除く3方のうち、2方が壁なら
                    end_p.append(i) # 候補リストに追加
        #print(end_p)
        if len(end_p): #候補が一つでもあれば
            i = rd.randint(0,len(end_p)-1) #リストのインデックスをランダムに選び
            #print(i)
            y = end_p[i] # y に代入
        else: #候補がない場合
            for i in range(height): #とりあえず右端から２列目の床のマスにゴールを設定
                if not self.maze_map[i][-2]:
                    y = i
        x = len(self.maze_map[-2])-2 #x座標を設定
        return(x, y) #設定した座標を返す
  
    def reset_maze(self):
        self.maze_map = maze_maker.make_maze(self.x,self.y)
        self.goal_pos = self.goal_p()

# %%
class Bird:
    def __init__(self, image, size, scr:Screen):
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rct = self.sfc.get_rect()
        self.size = size

        self.scr = scr
        self.tile_size = self.scr.tile_length

        self.xy = 1+1j
        self.rct.center = (int(self.xy.real)*self.tile_size+(self.rct.size[0]//2),int(self.xy.imag)*self.tile_size+(self.rct.size[1]//2))

    def update(self, scr):
        global stage_count
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
            self.rct.center = (int(self.xy.real)*self.tile_size+(self.tile_size//2),int(self.xy.imag)*self.tile_size+(self.tile_size//2))
        else:
            self.xy = tmp

        if self.xy == complex(self.scr.goal_pos[0],self.scr.goal_pos[1]):
            self.scr.reset_maze()
            stage_count += 1
            self.xy = 1+1j
            self.rct.center = (int(self.xy.real)*self.tile_size+(self.tile_size//2),int(self.xy.imag)*self.tile_size+(self.tile_size//2))
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
        self.xy = complex(self.scr.goal_pos[0],self.scr.goal_pos[1])
        self.rct.center = (int(self.xy.real)*self.tile_size+(self.tile_size//2),int(self.xy.imag)*self.tile_size+(self.tile_size//2))
        self.now_dir = 0
        self.count = 0
        self.interval = 5

    def update(self, scr:Screen):
        tmp = self.xy
        # クマの行動
        self.count += 1 #重兼修正 左手法実装
        if self.count > self.interval: #既定の間隔で
            self.now_dir, xy_real, xy_imag = self.search_left(scr.maze_map) 
            self.xy = complex(xy_real,xy_imag) #くまを動かす
            self.count = 0
            # 以下は同様
            if scr.maze_map[int(self.xy.imag)][int(self.xy.real)] != 1:
                self.rct.center = (int(self.xy.real)*self.tile_size+(self.tile_size//2),int(self.xy.imag)*self.tile_size+(self.tile_size//2))
            else:
                self.xy = tmp
        scr.sfc.blit(self.sfc,self.rct)

    def search_left(self, maze_map):#重兼追加 左手法実装
        dif = ((0,1), (1,0), (0,-1),(-1,0))
        for i in range(4):
            dir = (self.now_dir+3+i)%4
            x = (self.rct.centerx//int(self.tile_size) + dif[dir][0])
            y = (self.rct.centery//int(self.tile_size) + dif[dir][1])
            if maze_map[y][x] == 0:
                #print('d')
                break
            else:
                #print('f')
                pass
        return dir,x,y


# %%
class Text: #重兼修正
    def __init__(self, content, base_obj:Screen, x_size, y_size) -> None:
        font = pg.font.Font(None, 60)
        self.sfc = font.render(content, True, (255,0,0))
        self.rct = self.sfc.get_rect()
        self.rct.center = x_size//2, y_size//2
        base_obj.sfc.blit(self.sfc,self.rct) #文言を表示
    
    def blit(self, base_obj:Screen):
        base_obj.sfc.blit(self.sfc, self.rct)

# %%
class main():
    def __init__(self) -> None:
        global stage_count
        stage_count+=1
        running = True
        self.scr = Screen(17,9)
        kkt = Bird("ex06/6.png", tori_dia,self.scr)
        brs = [Bear("ex06/animal_kowai_kuma.png",kuma_dia,self.scr)]
        txt = Text(str(stage_count), self.scr, self.scr.tile_length//2, self.scr.tile_length//2)
        clock = pg.time.Clock()

        counter = 0


        while running:
            # ここにコードを書く
            print(stage_count)

            if counter > 500:
                brs.append(Bear("ex06/animal_kowai_kuma.png",kuma_dia,self.scr))
                counter = 0

            self.scr.draw_map()
            txt.blit(self.scr)
            kkt.update(self.scr)
            """ brs[0].update(scr) """
            for b in brs:
                b.update(self.scr)

            for b in brs:
                if kkt.rct.colliderect(b.rct):
                    self.game_over()
                    return


            # イベント処理部
            for event in pg.event.get():
                if event.type == pg.QUIT:  # 終了イベント
                    running = False
                    pg.quit()  #pygameのウィンドウを閉じる
                    sys.exit() #システム終了    
                    return
                if event.type == pg.KEYDOWN and event.key == pg.K_r:
                    main()   

            pg.display.update() #描画処理を実行
            counter += 1
            clock.tick(10)
    
    def game_over(self):
        if not pg.font.get_init:
            pg.font.init()
        font = pg.font.Font(None, 80)
        self.sfc = font.render(str("GAME OVER"), True, (255,0,0))
        self.rct = self.sfc.get_rect()
        self.rct.center = self.scr.rct.width/2,self.scr.rct.height/2
        self.scr.sfc.blit(self.sfc,self.rct) #文言を表示
        pg.display.update()
        while True: #バッテンが押されるまで無限ループ
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

# %%
if __name__ == '__main__':
    global stage_count
    stage_count = 0
    pg.init()
    main()
    pg.quit()
    sys.exit()


