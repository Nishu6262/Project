# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:20:35 2019

@author: BSDU ADMIN
"""

"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday ses most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
"""

import pandas as pd 
import numpy as np

data = pd.read_csv("thanksgiving-2015-poll-data.csv")

"""Convert the column name to single word names"""

cols = data.columns.tolist()
new = list(range(1,66))


dict1 ={}

for i in range(0,len(new)):
    dict1[cols[i]] = i

data.rename(columns=dict1, inplace=True) 


"""
Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income"""
    
    
data[62]=data[62].apply(lambda x: 0  if(x=='Male') else 1 )
   
""" 
(Range to a average number, X and up to X, Prefer not to answer to NaN)
"""


data[63] = data[63].astype(str)
data[63] = data[63].replace('Prefer not to answer',np.nan)

def salary(s):
    if 'to' in str(s):
        s = s.replace('$','')
        s = s.replace(',','')
        a,b = s.split(' to ')
        return((float(a)+float(b))/2)
    elif('$200,000 and up'):
        return int(200000)

data[63] = data[63].apply(salary)  




"""compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?"""
    
import pandas as pd
import matplotlib.pyplot as plt


homemade =(data[data[8]=='Homemade'][63]).mean()
canned =(data[data[8]=='Canned'][63]).mean()

  
plt.xticks([0,1],['Homemade','Canned'])
plt.bar([0,1],[homemade,canned],color=['Blue','black'])
plt.show()





"""find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc)."""


data[8].value_counts()
homemade =(data[data[8]=='Homemade'][63]).mean()
canned =(data[data[8]=='Canned'][63]).mean()
none =(data[data[8]=='None'][63]).mean()
others =(data[data[8]=='Other (please specify)'][63]).mean()


plt.pie([homemade,canned,others,none],labels=['Homemade','Canned','Other (please specify)','None'],autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.show()





"""    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
"""
Suburban = len(data[data[60]=='Suburban'][2])
Rural = len(data[data[60]=='Rural'][2])

plt.xticks([0,1],['Suburban','Rural'])
plt.bar([0,1],[Suburban,Rural],color=['red','green'])
plt.show()





"""
    Where do people go to Black Friday sales most often?
"""

black_fri_values = data[data[57]=='Yes'][64].value_counts().tolist()
black_fri_names = data[data[57]=='Yes'][64].unique().tolist()

black_fri_names.pop()

black_fri_names = tuple(black_fri_names)
# lets plot
plt.pie(black_fri_values,labels=black_fri_names)


"""
    Is there a correlation between praying on Thanksgiving and income?
"""
#Taking The mean
YesPray = data[data[51]=='Yes'][63].mean()
NotPray = data[data[51]=='No'][63].mean()

#Ploting the chart
plt.pie([YesPray,NotPray],labels=['Who Pray','Who Not Pray'],autopct='%1.1f%%',shadow=True, startangle=90)

"""
    What income groups are most likely to have homemade cranberry sauce?
"""
Incomes = data[data[8]=='Homemade'][63].value_counts().tolist()
valueincome = tuple(data[data[8]=='Homemade'][63].unique())

plt.pie(Incomes,labels=valueincome)




"""

Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes,
        but those who also have Roast Beef have the lowest incomes
"""


"""it will return all the values who has roast beef"""
data[data[2]=='Turducken'][[8,63,2]]

""" homemade average income"""

var_one = data[(data[2]=='Turducken') & \
           (data[8] == 'Homemade')
        ].mean()[63]

"""find all the values who has"""
data[data[2]=='Roast beef'][[63,8,2]]

"""average income of Canned"""
var_two = data[(data[8] == 'Canned') & \
               (data[63] == data[63])
        ].mean()[63]

"""average income of canned roast beef"""
var_three = data[(data[2] =='Roast beef') & \
               (data[8] == 'Canned') & \
               (data[63] == data[63])
        ].mean()[63]


"""store the incomes in the list"""
verify_val = [var_one,var_two,var_three]
"""lets plot the values of the"""
plt.pie(verify_val,labels=['Homemade','Canned','Roast Beef'])





























