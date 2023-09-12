#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:53:42 2023

@author: stevenschindler
"""

import random
import pylab


def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x -mean)**2
    return tot/len(X)
def stdDev(X):
    return variance(X)**0.5


def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.choice(('H','T')) == 'H':
            heads += 1
    return heads/float(numFlips)

def flipSim(numFlipsPerTrial,numTrial):
    fracHeads = []
    for i in range(numTrial):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd)


def labelPlot(numFlips,numTrial, mean, sd):
    pylab.title(str(numTrial) +' trials of' + str(numFlips)+' flips each')
    pylab.xlabel('Fraction of Heeads')
    pylab.ylabel('Number of Trials')
    pylab.annotate('mean = '+str(round(mean,4)) +'\nSD = ' + str(round(sd,4)), size = 'x-large',xycoords = 'axes fraction', xy = (0.67,0.5))

def makePlots(numFlips1,numFlips2,numTrial):
    val1,mean1,sd1 = flipSim(numFlips1, numTrial)
    pylab.hist(val1,bins = 20)
    xmin,xmax = pylab.xlim()
    
makePlots(50,200,1000)