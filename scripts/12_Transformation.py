#Transformations
 
import rhinoscriptsyntax as rs
import random
 
#Start off with a point
userPt = rs.GetPoint("create a point")
 
rs.EnableRedraw(False)

listOfPoints = []
 
for i in range(0,100):
    xDir = random.uniform(-10.0, 10.0)
    yDir = random.uniform(-10.0, 10.0)
    zDir = random.uniform(-10.0, 10.0)
    vect = (xDir, yDir, zDir)
    pt = rs.CopyObject(listOfPoints[-1],vect)
    listOfPoints.append(pt)

myPolyline = rs.AddPolyline(listOfPoints)

rs.Redraw()