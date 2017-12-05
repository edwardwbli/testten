from __future__ import print_function
import numpy as np
#import matplotlib as mp
#mp.use('Agg') #disable using DISPLAY 
#import matplotlib.pyplot as pl

customer1 = np.random.random((100,12))*10000
target1 = np.ones((100,1)) * 2
sample1 = np.hstack((customer1,target1))
print(sample1)

#pl.polar(customer1)
#pl.savefig('book5_read.png')
a = np.asarray(sample1)
np.savetxt("c1.csv", a, fmt="%10d",delimiter=",")

