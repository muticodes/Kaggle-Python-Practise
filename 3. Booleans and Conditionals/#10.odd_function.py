#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:10:39 2021

@author: Colin Moris
Code from Kaggle
"""
#Simple function which shows whether or not number is odd

def is_odd(n):
    return (n%2) == 1,

print("Is 100 odd", is_odd(100))
print("Is -1 odd", is_odd(-1))
