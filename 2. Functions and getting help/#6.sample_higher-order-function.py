#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Typed on Thu Jan 21 09:21:25 2021
Code copied from Kaggle
@author: mutimw
"""

def multi_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    return fn(fn(arg))

print(
      call(multi_by_five, 1),
      squared_call(multi_by_five, 1),
      sep = '\n', #Starts a new line
      )
