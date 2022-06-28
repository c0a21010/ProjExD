import tkinter as tk
import tkinter.messagebox as tkm

from matplotlib import image, widgets
from numpy import imag

import maze_maker

global key, cx, cy, mx, my
key = ""
cx = 300
cy = 400
mx = 1
my = 1

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

        mazelist = maze_maker.make_maze(15,9)

        maze_maker.show_maze(self.canvas,mazelist)


        self.kokaton = tk.PhotoImage(file="5.png")

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

        global cx, cy, mx, my

        cx_cy = complex(cx,cy)
        mx_my = complex(mx,my)

        if key in move.keys():

            # print(key)

            mx_my += move[key]

            mx = mx_my.real
            my = mx_my.imag

            # print(move[key])

            # print(cx_cy)

            cx = mx_my.real*100+50
            cy = mx_my.imag*100+50

            self.canvas.coords("kokaton",cx,cy)

        

        self.master.after(100,self.main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()