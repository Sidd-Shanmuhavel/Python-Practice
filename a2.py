# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:51:04 2019

@author: Siddhartha Shanmuhavel 

Student Id: 119220393

"""

'''
This program computes the syracuse sequence for any given positive integer.


The 1st function return the next number to n based on the odd/even criterion.
The 2nd function returns the length of the sequence and the longest number in that sequence.
The 3rd function computes the sequence for a series of numbers from n to 1 and return the 
starting point and the length of the longest sequence.

'''

# Calculate and Return the next number to n in the sequence
def syracuse_fn(n):
    # Checking if the number is even or not
    if n % 2 == 0:
        # returning half of n since it is an even number
        return n / 2
    # returning triple the value of n + 1 since it is an odd number
    return (n * 3) + 1
    

# Returning the length of the sequence and the biggest number in that sequence
def syracuse_seq(n):
    nextnumber = n
    biggestnumber = nextnumber
    length = 1
    # Checking if the  next number in the sequence is not 1
    while nextnumber != 1:
        # finding the next number in the sequence
        nextnumber = syracuse_fn(nextnumber)
        # finding the biggest number in the sequence
        if nextnumber > biggestnumber:
            biggestnumber = nextnumber
        # finding the length of the sequence
        length = length + 1
    return length, biggestnumber
    


# Calculating and returning the starting point and the length of the longest sequence from 1 to n
def longest_seq(n):
    biggestlen = 1
    startingpt = 1
    length = 1
    # finding the sequence for every number from 1 to n
    for i in range(1, n+1):
        x = i
        # making sure that the next number in the sequence is not 1
        while x != 1:
            # finding the next number in the sequence
            x = syracuse_fn(x)
            # finding the length of the sequence
            length = length + 1
        # finding the longest sequence and the length of that sequence
        if length > biggestlen:
            biggestlen = length
            startingpt = i
        # Resetting the value of length to the default value 1 for the next sequence
        length = 1
    return startingpt, biggestlen


    
