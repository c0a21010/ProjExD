import tkinter as tk
import tkinter.messagebox as tkm

from matplotlib import image, widgets
from numpy import imag

import maze_maker

global key, cx, cy
key = ""
cx = 300
cy = 400

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

        self.kokaton = tk.PhotoImage(file="5.png")

        self.canvas.create_image(cx,cy,image=self.kokaton,tag="kokaton")

        self.canvas.pack()

        self.master.bind("<KeyPress>", self.key_down)
        self.master.bind("<KeyRelease>", self.key_up)

        mazelist = maze_maker.make_maze(15,9)

        self.main_proc()

    def key_down(self,event):
        global key
        key = event.keysym
        # print(key)

    def key_up(self,event):
        global key
        key = ""

    def main_proc(self):
        move = {
            "Up":-20j,
            "Down":20j,
            "Left":-20,
            "Right":20,
        }

        global cx, cy

        cx_cy = complex(cx,cy)

        if key in move.keys():

            # print(key)

            cx_cy += move[key]

            # print(move[key])

            # print(cx_cy)

            cx = cx_cy.real
            cy = cx_cy.imag

            self.canvas.coords("kokaton",cx,cy)

        

        self.master.after(100,self.main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()