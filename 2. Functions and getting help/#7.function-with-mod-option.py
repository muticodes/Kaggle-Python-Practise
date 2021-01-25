#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:21:10 2021
code copied from Kaggle
@author: muticodes
By default, max returns the largest of its arguments. But if we pass in a 
function using the optional key argument, 
it returns the argument x that maximizes key(x) (aka the 'argmax').
"""

def mod_5(x):
    """returns remainder after dividing with 5"""
    return (x%5)

print(
      "Which number is the biggest", 
      max(100,71,14),
      "Which number is the biggest modulo 5?",
      max(100, 71, 14, key = mod_5),
      sep = '\n'
      )