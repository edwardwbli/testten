from __future__ import print_function
import numpy as np
import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as pl

customer1 = np.random.random((12,100))*5000
customer2 = np.random.random((12,100))*10000
customer3 = np.random.random((12,100))*50000
customer4 = np.random.random((12,100))*100000
print(customer1)

pl.polar(customer1)
pl.savefig('book5_read.png')
