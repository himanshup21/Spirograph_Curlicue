import numpy as np
import time
from graphics import*

s = 2**0.5
th = 0
phi = 0

ptx = [0]
pty = [0]

win = GraphWin('Curlicue',1000,1000, autoflush=False)
win.setCoords(-35,-20,10,20)

txt = Text(Point(-12.5,17),'s = e')
txt.setTextColor('black')
txt.setSize(15)
txt.draw(win)
win.update()


#time.sleep(15)
while True:
    phi = th + phi%(2*np.pi)
    th = (th+2*np.pi*s)%(2*np.pi)

    length = 2**(-3)
    x = ptx[-1] +  length*np.cos(phi)
    y = pty[-1] +  length*np.sin(phi)

    ptx.append(x)
    pty.append(y)
    
    L = Line(Point(ptx[-1],pty[-1]), Point(ptx[-2],pty[-2]))
    L.setFill('orange')
    L.draw(win)
    
    ptx.remove(ptx[0])
    pty.remove(pty[0])

    update(1000)    

