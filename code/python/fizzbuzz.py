# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:04:35 2019

@author: user
"""

def Fizzbuzz(max_size):
    for i in range(1, max_size+1):
        if i%3 == 0 and i%5 == 0:
            print("{}:Fizz Buzz".format(i))
        elif i%3 == 0:
            print("{}:Fizz".format(i))
        elif i%5 == 0:
            print("{}:Buzz".format(i))
        else:
            print("{}:".format(i))
            
Fizzbuzz(50)