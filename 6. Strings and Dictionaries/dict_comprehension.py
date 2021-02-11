#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 09:33:14 2021

@author: muticodes
"""
# Python has dictionary comprehensions with a syntax similar to the list 
# comprehensions we saw in the previous tutorial.

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_to_initial = {planet: planet[0] for planet in planets}
print(planets_to_initial)

# The in operator tells us whether something is a key in the dictionary