#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:05:21 2021

@author: muticodes
"""
#Program that rounds given number to two decimal points

def round_to_two_places(num):
    """Rounds any given number to decimal places using function round() and
    ndigits. ie ndigits = 2 rounds to nearest two decimal points. ndigits -2 next 100, etc
    
    >>>round_to_two_places(3.14159) = 3.14
    """
    return(round(num, ndigits=-2))

a = round_to_two_places(354897)
print(a)
