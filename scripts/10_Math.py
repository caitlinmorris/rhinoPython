import rhinoscriptsyntax as rs
import math
 
pointList = []
 
for i in rs.frange(0.0, 10.0, 0.1):
    
    x = i
    y = math.sin(i)
    z = 0.0
    
    #play with the math to create more complex shapes!
    #x = i*math.sin(i)
    #y = i*math.cos(i)
    #z = 0.0
    
    rs.AddPoint(x,y,z)
    
    pt = (x,y,z)
    pointList.append(pt)
 
curve = rs.AddCurve(pointList)