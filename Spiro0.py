import numpy as np
from graphics import*
import time

win = GraphWin('Spirograph',1000,1000, autoflush=False)
win.setCoords(-2,-2,2,2)

R = 1
r = 0.7
f = 0.8

ratio = round(R/r,3)


c0 = Circle(Point(0,0),R)
c1 = Circle(Point(R-r,0),r)

trace = Circle(Point(R-r+f*r,0),0.01)
trace.setFill('brown')

c0.draw(win)
c1.draw(win)
trace.draw(win)

th = 0

txt = Text(Point(0,1.4),'R/r = '+ str(ratio) + '\t'+'f = ' + str(f))
txt.setTextColor('black')
txt.setSize(20)
txt.draw(win)
win.update()

time.sleep(5)
while th <= 2*np.pi*7:

    pos = [c1.getCenter(), trace.getCenter()]
    
    x = (R-r)*np.cos(th)
    y = (R-r)*np.sin(th)

    xt = x + f*r*np.cos((R/r -1)*th)
    yt = y - f*r*np.sin((R/r -1)*th)

    c1.move(x-pos[0].getX(), y-pos[0].getY())
    trace.move(xt-pos[1].getX(), yt-pos[1].getY())

    t = trace.getCenter()
    t.setFill('brown')
    t.draw(win)

    th += 0.01
    update(200)


