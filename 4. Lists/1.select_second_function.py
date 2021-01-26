#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:09:41 2021

@author: mutimw
"""

def select_second(L):
    """Return the second element in a list. If the list has no second element,
    return none.
    """
    if len(L) < 2:
        return None 
    else:
        return L[1]