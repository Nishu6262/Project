# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:29:22 2019

@author: hp
"""

import socket
import uuid
import sys
import calendar
import random 


user9 = str(input("enter your user name(only str value)::>>"))
t = random.randint(1000,5000)
print(t)

user3 = int(input("enter your passowrd (only int value):>>"))

hostname = socket.gethostname()
user5=(sys.version)



IP = socket.gethostbyname(hostname)

yy = 2019
mm = 8

if(user3==t):
        
    print("\n your password is currect \n Thank you for login \n")

    print("your computer Name>>" ,hostname,"\n")
    
    print("your current dircety>>" , user5,"\n")
    
   
    print("your IP adress>> " , IP,"\n")

    print("your mack address>>" ,(hex(uuid.getnode())),"\n")
 
    print("current month calendar\n\n"  ,calendar.month(yy,mm))    
else:
    print("chek your password")
    


