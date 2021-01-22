#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 08:24:20 2021

@author: Colin Moris from Kaggle, muticodes
"""
# program that shares candy equally amongst three friends, smashing the rest

def to_smash(total_candy):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candy == 1:
        print("splitting one candy")
    else:
        print("splitting", total_candy, "left-over candies")
    
    return total_candy % 3

print("we will smash", to_smash(89), "candies")


