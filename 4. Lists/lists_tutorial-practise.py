#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:36:41 2021

@author: mutimw
"""

#List tutorial via Kaggle

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets[7] = 'Mutisunge' #Lists are mutable

print(planets)

#len() function
#sorted() function

primes = [2, 3, 5, 7]

print(sum(primes))

print(max(primes))


## Interlude: Objects

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)

# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

"""
The things an object carries around can also include functions. 
A function attached to an object is called a method. 
(Non-function things attached to an object, such as imag, are called 
attributes).
"""

# List methods
# Pluto is a planet darn it!
planets.append('Pluto')

#Searching lists
planets.index('Earth')

#'in' operator to determine whether a list contains a particular value
# Is Earth a planet?
"""
>>> "Earth" in planets
- True
"""

#Tuples
"""Tuples are often used for functions that have multiple return values.
For example, the as_integer_ratio() method of float objects returns a 
numerator and a denominator in the form of a tuple:
    
>>> x = 0.125
x.as_integer_ratio()
- (1, 8)

These multiple return values can be individually assigned as follows:

>>> numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)
- 0.125

Finally we have some insight into the classic Stupid Python Trick™ for swapping 
two variables!
>>> a = 1
>>> b = 0
>>> a, b = b, a
>>> print(a, b)
- 0 1
"""

