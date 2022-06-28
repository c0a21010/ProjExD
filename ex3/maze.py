import tkinter as tk
import tkinter.messagebox as tkm
import tkinter.font as tfont

from matplotlib import image, widgets
from numpy import block, imag

import maze_maker

global key, cx, cy, mx, my, my_block, mode
key = ""
cx = 150
cy = 150
mx = 1
my = 1
my_block = 0
mode = -1

class Application(tk.Frame):
    def __init__(self,master) -> None:
        super().__init__(master)

        self.master.geometry()


        # self.key = ""
        self.canvas = tk.Canvas(
            self.master,
            width = 1500,
            height = 900,
            bg="black"
        )

        self.mazelist = maze_maker.make_maze(15,9)

        print(self.mazelist)

        maze_maker.show_maze(self.canvas,self.mazelist)

        self.canvas.create_rectangle(100,100,200,200,fill="red")
        self.canvas.create_rectangle(1300,700,1400,800,fill="blue")

        self.kokaton = tk.PhotoImage(file="ex3/5.png")

        self.canvas.create_image(cx,cy,image=self.kokaton,tag="kokaton")

        self.canvas.pack()

        self.master.bind("<KeyPress>", self.key_down)
        self.master.bind("<KeyRelease>", self.key_up)

        self.main_proc()

    def key_down(self,event):
        global key
        key = event.keysym
        # print(key)

    def key_up(self,event):
        global key
        key = ""

    def main_proc(self):
        # move = {
        #     "Up":-20j,
        #     "Down":20j,
        #     "Left":-20,
        #     "Right":20,
        # }

        move = {
            "Up":-1j,
            "Down":1j,
            "Left":-1,
            "Right":1,
        }

        global cx, cy, mx, my,mode,myblock

        cx_cy = complex(cx,cy)
        mx_my = complex(mx,my)


        if key in move.keys():

            # print(key)

            next = mx_my + move[key]

            print(next,mx_my)
            print(next.real
            ,next.imag)
            # print(self.mazelist[int(next.real)][int(next.imag)])

            if mode > 0:
                print("zikkou")
                self.set_block(next.real,next.imag)

            elif self.mazelist[int(next.imag)][int(next.real)] == 0:

                mx_my = next

                mx = mx_my.real
                my = mx_my.imag

                # print(move[key])

                # print(cx_cy)

                cx = mx_my.real*100+50
                cy = mx_my.imag*100+50

                self.canvas.coords("kokaton",cx,cy)
            
            else:
                self.dig(next.real,next.imag)


        if key == "Shift_L":
            mode *= -1


        self.master.after(100,self.main_proc)



    def dig(self,arg_x,arg_y):
        global my_block
        x = int(arg_x)
        y = int(arg_y)

        print(x,y)

        if self.mazelist[y][x] == 1:
            self.mazelist[y][x] = 0
            new_zimen = self.canvas.create_rectangle(x*100,y*100,x*100+100,y*100+100,fill="green")
            self.canvas.lift("kokaton",new_zimen)

            my_block += 1

    def set_block(self,arg_x,arg_y):
        global my_block

        x = int(arg_x)
        y = int(arg_y)

        if self.mazelist[y][x] == 0:
            self.mazelist[y][x] = 1
            new_zimen = self.canvas.create_rectangle(x*100,y*100,x*100+100,y*100+100,fill="blue")
            self.canvas.lift("kokaton",new_zimen)

            my_block += 1


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()