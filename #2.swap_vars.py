# -*- coding: utf-8 -*-
"""
Spyder Editor
# 2. Add code to the following cell to swap variables a and b 
# (so that a refers to the object previously referred to by b and vice versa).
"""
a = [1,2,3]
b = [3,2,1]

temp = a
b = temp
a = b

print(a)
print(b)
