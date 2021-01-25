#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 08:02:42 2021

@author: colin Moris from Kaggle
"""

#Boolean conversion

print(bool(1)) #All numbers are true except for 0
print(bool(0)) #
print(bool("abc")) #all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see 
# like lists and tuples) are "falsey" and the rest are "truthy"