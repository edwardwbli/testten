import numpy as np
import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as pl

customer1 = np.random.random((12,))
customer2 = np.random.random((12,))
customer3 = np.random.random((12,))
customer4 = np.random.random((12,))

pl.plot(customer1*1000)
pl.plot(customer2*5000)
pl.plot(customer3*10000)
pl.plot(customer4*20000)

pl.savefig('book4_read.png')
