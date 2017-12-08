from __future__ import print_function
import matplotlib as mp
mp.use('Agg') #disable using DISPLAY 
import matplotlib.pyplot as pl
import demjson

arrlist = []
with open('test.txt') as fl: 
	for line in fl: 
		j = demjson.decode(line);
		arrlist.append(j['accuracy'])

pl.plot(arrlist);
pl.savefig('trend.png')
