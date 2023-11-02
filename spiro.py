import numpy as np
from graphics import*
import time

win = GraphWin('Spirograph',1000,1000, autoflush=False)
win.setCoords(-10.2,-10.2,10.2,10.2)

R = [2**i for i in range(1,-5,-1)]
print(len(R))
circles = [Circle(Point(0,0),R[0])]
for i in range(1,len(R)):
    circles.append(Circle(Point(circles[-1].getCenter().getX()+R[i-1]+R[i],0),R[i]))

trace = Circle(Point(2*sum(R)-R[0],0),0.001)
trace.setFill('red')
trace.draw(win)



for i in range(len(circles)) :
    circles[i].setOutline('gray')
    circles[i].draw(win)

omega = [0]*len(R)
dt = [(-4)**n for n in range(-(len(R)),0)]

cnt = 0
#time.sleep(20)
while True:

    for i in range(1,len(circles)):

        pos = [c.getCenter() for c in circles]
        
        
        x = pos[i-1].getX() + (R[i]+R[i-1])*np.cos(omega[i])
        y = pos[i-1].getY() + (R[i]+R[i-1])*np.sin(omega[i])
        
        circles[i].move(x-pos[i].getX(), y-pos[i].getY())

        if i == len(circles)-1:
            t = trace.getCenter()
            
            xt = x - R[i]*np.cos((R[i]+R[i-1])*omega[i]/R[i])
            yt = y - R[i]*np.sin((R[i]+R[i-1])*omega[i]/R[i])
            
            trace.move(xt-t.getX(), yt-t.getY())


            t.setFill('orange')
            t.draw(win)

            cnt += 1

        omega[i] += dt[i]
        


    update(100)
    win.update()

      

