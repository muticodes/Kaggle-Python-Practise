#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:37:24 2021

@author: Colin Moris
Additional input by Muticodes
"""
def prepared_for_weather (have_umbrella, rain_level, have_hood, is_workday):
    return(have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday)
    
have_umbrella = False
rain_level = 4
have_hood = False 
is_workday = False
    
Actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(Actual)

"""
Solution: One example of a failing test case is:

have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False
Clearly we're prepared for the weather in this case. It's not raining. Not only that, it's not a workday, so we don't even need to leave the house! But our function will return False on these inputs.

The key problem is that Python implictly parenthesizes the last part as:

(not (rain_level > 0)) and is_workday
Whereas what we were trying to express would look more like:

not (rain_level > 0 and is_workday)
"""
