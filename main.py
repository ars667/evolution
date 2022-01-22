import random
import tkinter
from tkinter import *

rad = 25
x = 100
y = 200


def oval(x,y):
    oval = c.create_oval(
        x - rad, y - rad, x + rad, y + rad, outline="#111",
        fill="#fff", width=2
    )


def main(x, y):
    oval(x, y)
    window.update()
    for i in range(10):
        window.after(500, c.delete(oval(x,y)))
        window.update()
        x1 = random.randint(-1,1)*25
        y1 = random.randint(-1,1)*25
        x += x1
        y += y1
        oval(x, y)
        window.update()


window = Tk()
window.title('evolution')
window.geometry('850x600+75+20')
window.resizable(0, 0)
window.iconbitmap('icon.ico')
c = Canvas(window, width=850, height=600, bg='white')
button1 = tkinter.Button(window, text="СТАРТ", command=main(x, y))
button1.pack()
c.pack()
window.mainloop()
