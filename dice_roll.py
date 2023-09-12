#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 13:50:23 2023

@author: stevenschindler
"""

import random
def rollDie():
    return random.choice([1,2,3,4,5,6])
def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)
    
rollN(5)