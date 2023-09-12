#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:06:10 2023

@author: stevenschindler
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
N = norm.cdf

def BS_CALL(S,K,T,r,sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/sigma * np.sqrt(T)
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K*np.exp(-r*T)*N(d2)

def BS_PUT(S,K,T,r,sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/sigma * np.sqrt(T)
    d2 = d1 - sigma * np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)


K = 10
r = 0.1
S = 10
sigma = 0.3

T = np.arange(0,2,0.01)# array range
calls = [BS_CALL(S,K, T, r, sigma) for t in T] #array of series of option value
puts = [BS_PUT(S,K, T, r, sigma) for t in T] #array of series of option value
plt.plot(T,calls,label = 'Call value')
plt.plot(T,puts,label = 'put value')
plt.xlabel('Stock Price')
plt.ylabel('Option Value')
plt.title('Impact of Timee to maturity')
plt.legend()
