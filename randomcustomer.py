from __future__ import print_function
import numpy as np
#import matplotlib as mp
#mp.use('Agg') #disable using DISPLAY 
#import matplotlib.pyplot as pl

customer1 = np.random.random((100,12))*5000
target1 = np.ones((100,1))
sample1 = np.hstack((customer1,target1))

customer2 = np.random.random((100,12))*10000
target2 = np.ones((100,1)) * 2   
sample2 = np.hstack((customer2,target2))

customer3 = np.random.random((100,12))*20000
target3 = np.ones((100,1)) * 3    
sample3 = np.hstack((customer3,target3))

customer4 = np.random.random((100,12))*50000
target4 = np.ones((100,1))    
sample4 = np.hstack((customer4,target4))
#pl.polar(customer1)
#pl.savefig('book5_read.png')
a = np.asarray(sample1)
np.savetxt("c1.csv", sample1, fmt="%10d",delimiter=",")
np.savetxt("c2.csv", sample2, fmt="%10d",delimiter=",")
np.savetxt("c3.csv", sample3, fmt="%10d",delimiter=",")
np.savetxt("c4.csv", sample4, fmt="%10d",delimiter=",")
