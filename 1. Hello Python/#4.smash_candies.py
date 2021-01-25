#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 07:23:41 2021

@author: mutimw
"""
# 4. Alice, Bob and Carol have agreed to pool their Halloween candy and split 
# it evenly among themselves. For the sake of their friendship, any candies 
# left over will be smashed. For example, if they collectively bring home 
# 91 candies, they'll take 30 each and smash 1.
# Write an arithmetic expression below to calculate how many candies they must 
# smash for a given haul.

alice_candies = 121
bob_candies = 77
carol_candies = 109

to_smash = (alice_candies + bob_candies + carol_candies)%3 
#Modulus function will give us integer remainder
print(to_smash)
