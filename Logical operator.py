# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:39:08 2021

@author: Lujain
"""
a=int(input())
b=int(input())
c=int(input())
if a>b and c>a:
    print("Both conditions are true")
elif a>b or a>c:
    print("At least one of the condition is true")