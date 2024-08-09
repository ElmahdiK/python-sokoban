"""
Created on 2024-08-09
@author Elmahdi KORFED
"""

from tkinter import *

root = Tk()
root.title("Sokoban python")
root.geometry("700x700")

BOX_WIDTH=50

my_canvas = Canvas(root, width=500, height=500, bg="whitesmoke")
my_canvas.pack(pady=50)


rect = my_canvas.create_rectangle(0, 0, BOX_WIDTH, BOX_WIDTH, fill="silver", outline="")
my_canvas.move(rect,3*BOX_WIDTH,3*BOX_WIDTH)

def up(event):
    x=0
    y=-BOX_WIDTH
    my_canvas.move(rect,x,y)

def down(event):
    x=0
    y=BOX_WIDTH
    my_canvas.move(rect,x,y)

def right(event):
    coors = my_canvas.coords(rect)
    if (coors[0] < 450):
        x=BOX_WIDTH
        y=0
        my_canvas.move(rect,x,y)
    print(coors[0])

def left(event):
    coors = my_canvas.coords(rect)
    if (coors[0] > 0):
        x=-BOX_WIDTH
        y=0
        my_canvas.move(rect,x,y)
    print(coors[0])

root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<Left>', left)
root.bind('<Right>', right)




root.mainloop()