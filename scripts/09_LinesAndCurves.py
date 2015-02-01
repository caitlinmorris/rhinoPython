import rhinoscriptsyntax as rs
import random
 
pointList = []

for i in range(0,100):
    x = random.uniform(0,100)
    y = random.uniform(0,100)
    z = random.uniform(0,100)
    
    pt = [x,y,z]
 
    pointList.append(pt)
    
#for x in pointList:
#    rs.AddPoint(x)
 
handleCurve = rs.AddCurve(pointList)
interpCurve = rs.AddInterpCurve(pointList)
 
color_1 = [0,255,255]
color_2 = [255,0,255]
 
rs.ObjectColor(handleCurve, color_1)
rs.ObjectColor(interpCurve, color_2)