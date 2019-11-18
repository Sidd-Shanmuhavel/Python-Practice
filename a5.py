# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:04:33 2019

@author: Siddhartha Shannmuhavel

@id: 119220393
"""


'''Returns the list of elements in the numeric list numlist
which exceed all previous elements.'''
def peak(numlist):
    big = numlist[0]
    l1 = []
    for i in numlist:
        if i >= big and i not in l1:
            l1.append(i)
            big = i
    return l1

#Returns True if the integer n a perfect cube and False otherwise
def is_cube(n):
    absolutevalue = abs(n)
    for i in range(0,absolutevalue+1):
        if i**3 == absolutevalue:
            return True
    return False

#Return the smallest cube which exceeds the non-negative integer n
def first_cube_above(n):
    if n>=0 :
        number = abs(n)+1
        nextcube = 0
        notfoundnextcube = True
        #loop runs until a cube is not found
        while(notfoundnextcube):
            for i in range(0,number+1):
                if i**3 <= abs(n):
                    number = number +1
                else:
                    nextcube = i**3
                    notfoundnextcube = False
                    break
        return nextcube
    else:
        return "Please enter a non-negative integer"
