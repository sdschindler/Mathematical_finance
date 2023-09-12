#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:30:30 2023

@author: stevenschindler
"""

import random
import pylab

def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.choice(('H','T')) == 'H':
            heads += 1
    return heads/numFlips

def flipSim(numFlipsPerTrial,numTrial):
    fracHeads = []
    for i in range(numTrial):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean

print(flipSim(10,1))


def regressToMean(numFlips, numTrials):
    fracHeads = []
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    extremes, nextTrial = [], []
    for i in range(len(fracHeads)-1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrial.append(fracHeads[i+1])

            
regressToMean(15, 40)