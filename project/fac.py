# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 03:41:50 2019

@author: Nishu Sharma
"""

a = 0
b = 1

print(a)
print(b)

for i in range(1,5):
    i = a+b
    a=b
    b=i
    print(i)
    
       
#try:
#    from googlesearch import search
#except ImportError:
#    print("No module name")
#    
#query = "Bhartiya skill development university jaipur"
#
#for j in search(query , tld="co.in"):
#    print(j)
#    