import rhinoscriptsyntax as rs

myPoints = []

point_1 = (0, 0, 0)
point_2 = (10, 10, 10)

myPoints.append(point_1)
myPoints.append(point_2)

print myPoints

rs.AddPoint(myPoints[0])
rs.AddPoint(myPoints[1])