# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:51:58 2021

@author: vishal
"""
x=int(input("plz enter the year "))

def chk_leap_year(x):
    if(x%4 ==0):
       return print("leap year")
        
chk_leap_year(x)