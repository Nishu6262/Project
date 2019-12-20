# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:13:26 2019

@author: Nishu Sharma
"""

"""
Code Challenges
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Let's suppose you need to create a new dictionary from a given dictionary 
but with items that are greater than 2

In the problem above, what if you have to not only get the items greater than 2 
but also need to check if they are multiples of 2 at the same time. 

"""

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

new_dict = {key: val for key, val in dict1.items() if val > 2 if val%2==0}
print(new_dict)
