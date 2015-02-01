import rhinoscriptsyntax as rs
import math

srfSize = 5
offset = 10
multiList = []
srfList = []

rs.EnableRedraw(False)

for i in range(0,100,offset):
	for j in range(0,100,offset):

		pt1 = (i,j,0)
		pt2 = (i+srfSize, j, 0)
		pt3 = (i+srfSize, j+srfSize, 0)
		pt4 = (i, j+srfSize, 0)

		srfList.append(pt1)
		srfList.append(pt2)
		srfList.append(pt3)
		srfList.append(pt4)

		print srfList

		multiList.append(srfList)
		srfList = []
	
for i in range(0,len(multiList)):
	rs.AddSrfPt(multiList[i])
	
rs.Redraw()
	