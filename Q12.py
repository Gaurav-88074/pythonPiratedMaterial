import matplotlib.pyplot as pl
import numpy as np
y= [4,2,4,6,7,2,9,1]
x= list(range(1,len(y)+1))
pl.bar(x,y)
pl.xlabel("x-axis")
pl.ylabel("y-axis")

pl.show()
