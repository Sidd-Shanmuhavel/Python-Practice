# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:53:08 2019

@author: Siddhartha Shanmuhavel (119220393)
"""
# Calculate the e power of any given value
def expo(): 
    # Getting the real number as input from user
    a=int(input("Enter a real number :"))
    sum = 1
    f=1
    term=1
    # iterating for 100 times
    for i in range(1, 100):
        # calculating the factorial
        for j in range(i, 0, -1):
            f=f * j
        # calculating every term in the series seperately
        term = (a ** i) / f
        # calculating the sum of all terms
        sum=sum+term
        # resetting their values to the default value 1
        term=1
        f=1
    return sum
    
print(expo())
        