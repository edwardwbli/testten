from __future__ import print_function
import numpy as np
#import matplotlib as mp
#mp.use('Agg') #disable using DISPLAY 
#import matplotlib.pyplot as pl

customer1 = np.random.random((100,12))*5000
print(customer1)

#pl.polar(customer1)
#pl.savefig('book5_read.png')
a = np.asarray(customer1)
np.savetxt("c1.csv", a, fmt="%10.2f",delimiter=",")

