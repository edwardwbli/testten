import numpy as np
import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as pl

customer1 = np.random.random((12,100))*1000
customer2 = np.random.random((12,100))*1000
customer3 = np.random.random((12,100))*1000
customer4 = np.random.random((12,100))*1000

pl.plot(customer1)
pl.plot(customer2)
pl.plot(customer3)
pl.plot(customer4)

pl.savefig('book5_read.png')
