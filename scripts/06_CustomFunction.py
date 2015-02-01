import rhinoscriptsyntax as rs
import random
 
def drawSphere(x,y,z,r,g,b):
    rad = random.randint(5,10)
    pt = (x,y,z)
    thisColor = [r,g,b]
    sphere = rs.AddSphere(pt, rad)
    rs.ObjectColor(sphere, thisColor)
 
 
rs.EnableRedraw(False)
step = 30

for x in range(0,256, step):
    for y in range(0,256, step):
        for z in range(0,256,step):
            drawSphere(x,y,z,x,y,z)
            
rs.Redraw()