#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 08:13:47 2021

@author: muticodes
"""
# function called sign which takes a numerical argument and returns -1 if it's 
# negative, 1 if it's positive, and 0 if it's 0

def sign(num):
    if num < 0:
        return "Number is negative"
    elif num > 0:
        return "Number is positive"
    else:
        return "Number is zero"

print(sign(-4))

