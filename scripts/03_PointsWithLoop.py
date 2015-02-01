import rhinoscriptsyntax as rs

myPoints = []

for i in range(0,10):
    point = (i, i, i)
    myPoints.append(point)

for i in myPoints:
    rs.AddPoint(i)