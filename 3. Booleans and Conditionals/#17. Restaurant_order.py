#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:27:01 2021

@author: mutimw
"""
#The boolean variables ketchup, mustard and onion represent whether a customer 
#wants a particular topping on their hot dog. Implement a number of 
#boolean functions that correspond to some yes-or-no questions about the 
#customer's order

def placed_order(ketchup, mustard, onion):
    return ketchup or mustard or onion

ketchup = True
mustard = True
onion = False 


order = (placed_order (ketchup, mustard, onion))
print(order)