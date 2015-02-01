import rhinoscriptsyntax as rs
import random

for i in range(40):
    #randY = random.random()
    #randY = random.randint(5,40)
    randY = random.uniform(5,40)
    pt = (i, randY, 0)
    
    rs.AddPoint(pt)