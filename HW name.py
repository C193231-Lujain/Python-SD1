# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:43:37 2021

@author: Lujain
"""
name=str(input())
if len(name)<3:
    print("name must be at least 3 characters")
elif len(name)>50:
    print("name can be a maximum of 50 characters long")
else:
    print("name looks good!")