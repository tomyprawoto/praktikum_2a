# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:03:43 2019

@author: Habib Abdul R
"""

a = 3
b = "6"

try:
    c = a + b
    print(c)
except TypeError:
    print("Tipe data nya berbeda")