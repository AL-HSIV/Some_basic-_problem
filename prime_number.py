# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:59:09 2021

@author: vishal
"""

x = int(input("Plz Enter the number u want to check"))

def chk_prime(x):
    print("lovw")
    for i in range(2,x):
        if(x%i == 0):
            
            break
    print(i)
    if(i==x-1):
        print("prime")
    else:
        print("not a prime")
        
chk_prime(x)   
    
