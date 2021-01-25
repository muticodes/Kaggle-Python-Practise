#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:45:03 2021
code from Kaggle
@author: Colin Moris
"""
def can_run_for_presidency(age):
    return age >=35,

print("Can a 19-year old run for presidency?", can_run_for_presidency(19))
print("Can a 40-year-old run for Presidency in the US?", can_run_for_presidency(40))