from tkinter import *

def drawCirle(x, y, r):
    global count
    count += 1
    canvas.create_oval(x-r,y-r,x+r,y+r)
    canvas.create_text(x,y-r,text=str(count), font=('', 30))
    if r >= radius/2:
        drawCirle(x-r//2, y, r//2)
        drawCirle(x+r//2, y, r//2)

count = 0
wSize = 1000
radius = 400

window = Tk()
canvas = Canvas(window, height=1000, width=1000, bg='white')
drawCirle(wSize//2,wSize//2, radius)

canvas.pack()
window.mainloop()