# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:46:58 2019

@author: hp
"""

import matplotlib
import matplotlib.pyplot as abhi


grid = abhi.GridSpec(2,2 , wspace = 0.6 , hspace = 0.6)

year = [1980,1985,1990,1995,2000,2005,2010,2015]

INDIA = [10,0,30,25,50,60,70,80]

USA = [5,10,17,20,15,30,35,40]

UK = [8,16,24,2,40,48,56,64]

CHAINA = [5,9,3,7,8,6,7,3]


abhi.subplot(grid[0,0])
abhi.plot(year,INDIA , label ="INDIA" , color="r")
abhi.legend()
abhi.title("Poplation of INDIA ")
abhi.xlabel("Year")
abhi.ylabel("Poplation")


abhi.subplot(grid[0,1])
abhi.scatter(year,USA , label ="USA" , color ="g")
abhi.legend()
abhi.title("Poplation of USA ")
abhi.xlabel("Year")
abhi.ylabel("Poplation")



abhi.subplot(grid[1,0])
abhi.bar(year,UK , label ="UK" , color ="b")
abhi.legend()
abhi.title("Poplation of UK ")
abhi.xlabel("Year")
abhi.ylabel("Poplation")


abhi.subplot(grid[1,1])
abhi.bar(year,CHAINA , label ="CHINA" )
abhi.legend()
abhi.title("Poplation of CHINA ")
abhi.xlabel("Year")
abhi.ylabel("Poplation")


abhi.show()
