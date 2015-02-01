import rhinoscriptsyntax as rs
import random
import math

bToggle = False

diam_1 = 8
diam_2 = 3

for j in range(0, 100, 10):
    for i in range(0,100,10):
      pt = (i,j,0)
      if bToggle == True:
          diam = diam_1
          bToggle = False
      elif bToggle == False:
          diam = diam_2
          bToggle = True
      rs.AddCircle(pt, diam)