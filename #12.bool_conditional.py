#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:45:16 2021

@author: Colin Moris
"""
#Simple programs. Combines boolean and conditionals

def f(x):
    if x > 0:
        print("Only printed when x is positive; x = ",x)
        print("Also only printed when x is positive; x = ", x)
    print("Always printed, regardless of the value of x; x = ", x)

f(1)
f(0)