#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:21:04 2021

@author: Colin Moris
"""
#Boolean function which checks qualification for running for US presidency
#Based on age and whether one is a natural citizen

def can_run_for_presidency (age, is_a_natural_citizen):
     return is_a_natural_citizen and (age >=35),
     """Can someone of the given age and citizenship status run for president
       in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at 
    # least 35 years old
   

print(can_run_for_presidency(19, True))
print(can_run_for_presidency(55, False))
print(can_run_for_presidency(55, True))