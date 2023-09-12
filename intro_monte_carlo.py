#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:43:27 2023

@author: stevenschindler
"""

import random
import pylab

vals = []
for i in range(1000):
    num1 = random.choice(range(0,151))
    num2 = random.choice(range(0,151))
    vals.append(num1+num2)
pylab.hist(vals,bins=15)
pylab.xlabel('num of occurences')