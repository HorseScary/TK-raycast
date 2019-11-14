import math
from tkinter import *

m = [ [1,1,1,1,1,1,1,1,1,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,1,1,1,1,1,1,1,1,1] ]


size = '400x250'

px = 50
py = 50
lx = 150
ly = 60
fx = px
fy = lx

a = int(input('-->'))

window = Tk()
window.geometry(size)

c=Canvas(window, width=400, height=250)
c.pack()

lx = 100 * math.sin(a) + px
ly = 100 * math.cos(a) + px
fx = 100 * math.sin(a - 45) + px
fy = 100 * math.cos(a - 45) + px

c.create_line(px, py, lx, ly)
c.create_line(px, py, fx, fy)
a += 1
mainloop()
