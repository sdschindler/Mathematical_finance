#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:22:16 2023

@author: stevenschindler
"""
import numpy as np

K = 100
S = 100
r = 0.1
sigma = 0.3

def optDelta(q,T):
    d1 = ((np.log(S/K)+((r-q)+sigma**2/2)*T)) / (sigma*np.sqrt(T))
    return np.exp(-q*T) * d1 * 100


print(optDelta(0.05,1))