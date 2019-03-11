# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:51:16 2019

@author: PERSONAL
"""

#Keterampilan Penanganan Error
a = 3
b = "6"

try:
    c = a + b
    print(c)
except TypeError:
    print("Tipe data nya berbeda")