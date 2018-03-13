#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
from tkinter import Tk, Canvas, Frame, BOTH, Spinbox, Label, Button
from math import sqrt
 
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
        self.parent.title("Lines")        
        self.pack(fill=BOTH, expand=1)

        a_label = Label(
            self,
            text="Enter a:",
            font=("Purisa", 15)
        )
        a_label.pack()

        a_value = Spinbox(
            self,
            from_=-10,
            to = 10,
            textvariable=0,
            font=("Purisa", 10)
        )
        a_value.pack()

        calc_btn = Button(
            self,
            text="Build",
            font=("Purisa", 12),
            command=self.calculate_vars
        )
        calc_btn.pack()

        self.draw_coords_system()
        
 
    def draw_coords_system(self):
        y_start_x = 250
        y_start_y = 35
        y_finish_y = 300

        x_start_x = 50
        x_finish_x = (y_finish_y + y_start_y) / 2
        x_start_y = 450

        coord_start = (y_start_x - 1, x_finish_x)

        canvas = Canvas(self)
        canvas.create_line(y_start_x, y_start_y, y_start_x, y_finish_y, arrow='first') # Y
        canvas.create_line(x_start_x, x_finish_x, x_start_y, x_finish_x, arrow='last')  # X
        canvas.create_text(y_start_x - 10, y_start_y + 5, font=("Purisa", 15), text="Y")  # Y-label
        canvas.create_text(x_start_y - 5, x_finish_x + 20, font=("Purisa", 15), text="X") # X-label
        canvas.create_oval(coord_start[0] - 2, coord_start[1] - 2, coord_start[0]+ 4, coord_start[1] + 4, fill="black") # start-coord point
        canvas.create_text(coord_start[0] + 10, coord_start[1] + 20, font=("Purisa", 15), text="O")

        canvas.pack(fill=BOTH, expand=1)

    def calculate_vars(self):
        print('lol')

def main():
    root = Tk()
    ex = Example(root)
    root.geometry("500x500")
    root.mainloop()  
 
if __name__ == '__main__':
    main()