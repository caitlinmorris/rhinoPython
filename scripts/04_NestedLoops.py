import rhinoscriptsyntax as rs

maxVal = 100
step = 10

for x in range(0,maxVal,step):
    for y in range(0,maxVal,step):
        for z in range(0,maxVal,step):
            rs.AddPoint(x,y,z)