#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 09:06:05 2021

@author: mutimw
"""
def least_difference(a,b,c):
    """Return the least difference between any two numbers among a,b,and c
    
    >>> least_difference(5,78,12)
    7
    """
    
    diff1 = abs(a - b)
    diff2 = abs(a - c)
    diff3 = abs(b - c)
    return min(diff1,diff2,diff3)

print(
      least_difference(234,657,90),
      least_difference(786,564,98),
      least_difference(56,76,546)
      )
