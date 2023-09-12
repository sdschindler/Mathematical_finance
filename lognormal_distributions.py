import scipy
from scipy.stats import lognorm
import numpy as np
import pylab as pl

stddev = 0.8
mean = 0.4
dist = lognorm([stddev],loc=mean)
x = np.linspace(0,6,200)
print(pl.plot(x,dist.pdf(x)))
print(pl.plot(x,dist.cdf(x)))

import matplotlib.pyplot as plt
mu , sigma = 3. , 1. # meean and std dev
s = np.random.lognormal(mu,sigma,1000)
counts,bins,ignored = plt.hist(s, 100,density=True,align = 'mid')
x = np.linspace(min(bins),max(bins),10000)
pdf = (np.exp(-(np.log(x)-mu)**2)/2*sigma**2)/(x*sigma*np.sqrt(2*np.pi))
plt.plot(x,pdf,linewidth=2,color='r')
plt.axis('tight')
plt.show()
