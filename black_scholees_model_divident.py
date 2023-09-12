#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:54:25 2023

@author: stevenschindler
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
N = norm.cdf

def BS_CALL_D(S,K,T,r,q,sigma):
    d1 = (np.log(S/K) + (r-q + sigma**2/2)*T)/sigma * np.sqrt(T)
    d2 = d1 - sigma * np.sqrt(T)
    return S * np.exp(-q*T)*N(d1) - K*np.exp(-r*T)*N(d2)



K = 100
r = 0.1
T = 1
sigma = 0.3
q = .05

S = np.arange(60,140,0.1)# array range
callsD = [BS_CALL_D(s,K, T, r, q,sigma) for s in S] #array of series of option value


plt.plot(S,callsD,label = 'Call value')
#plt.plot(S,puts,label = 'put value')
plt.xlabel('Stock Price')
plt.ylabel('Option Value')
plt.title('Impact of BSM of S')
plt.legend()
