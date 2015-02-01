import rhinoscriptsyntax as rs
import random

xOffset = 3
yOffset = 4
count = xOffset, yOffset

points = []

for i in range(0, count[0]):
    for j in range(0, count[1]):
        z = random.uniform(-5,5)
        pt = i*xOffset, j*yOffset, z
        points.append(pt)
        
rs.AddSrfPtGrid(count, points)