# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:56:56 2021

@author: vishal
"""

a= int(input("enter coefficient of x**2"))
b= int(input("enter coefficient of x"))
c= int(input("enter constant value"))
x={-b-(b**2-4*a*c)**0.5}/2*a
y={-b+(b**2-4*a*c)**0.5}/2*a
print(x)
print(y)