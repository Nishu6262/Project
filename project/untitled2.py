# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 08:18:19 2019

@author: Nishu Sharma
"""

import pandas as pd 

#new = [18,20,16,52]
#new2 = [15,65,26,5]
#
#room = ['Big' , 'Normal' , 'Big' , 'Normal']
#data = pd.DataFrame({'Length': new , 'Breadth':new2 ,'Type':room})
#print(data)
#data['Area'] = data['Length'] * data['Breadth']
#
#print(data)


#age = [10,20,65,95,65]
#city = ['CityA' , 'CityB' , 'CityC' , 'CityD' ,'CityE']
#
#data = pd.DataFrame({'Age': age , 'City': city})
#
#print(data)
#
#dummy = pd.get_dummies(data['City'])
#
#data_age = pd.DataFrame(data=data , columns =['age'])
#
#data_mod = pd.concat([data_age.reset_index(drop=True),dummy] , axis =1)
#print(data_mod) 

M = [18,20,16,52]
E = [15,65,26,5]
H = [10,20,65,95]

g = ['A' , 'B' , 'C' ,'D']

d = pd.DataFrame({'Math' : M , 'English' :E , 'Hindi' : H})
print(d)







 