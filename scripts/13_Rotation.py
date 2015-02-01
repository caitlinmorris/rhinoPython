import rhinoscriptsyntax as rs

degrees = 30
numCurves = 12

ln = rs.GetCurveObject("Pick a line")

#print ln

for i in range(0, numCurves):
    
   # pt = rs.CurveEndPoint(ln[0])
    pt = (0,0,0)
    nl = rs.RotateObject(ln[0], pt, degrees * i, (0,0,1), True)
    #nl2 = rs.MoveObject(nl, [i,0,0])
