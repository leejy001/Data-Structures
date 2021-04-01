from tkinter import *
import random

def drawCirle(x, y, r):
    canvas.create_oval(x-r,y-r,x+r,y+r, width=2, outline=random.choice(colors))
    if r >= 20:
        drawCirle(x-r//2, y, r//2)
        drawCirle(x+r//2, y, r//2)

colors = ["red", "green", "blue", "black", "orange", "indigo", "violet"]
wSize = 1000
radius = 400

window = Tk()
canvas = Canvas(window, height=wSize, width=wSize, bg='white')
drawCirle(wSize//2, wSize//2, radius)

canvas.pack()
window.mainloop()