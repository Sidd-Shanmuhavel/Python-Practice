# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:57:59 2019

@author: Siddhartha Shanmuhavel

@id: 119220393
"""
'''This program is to find if a given string is palindrome or not'''


''' The Function gets a string as input and returns True 
or False if it is a palindrome or not'''

def is_palindrome(s):
    s1 = ""
    reverse = ""
    #Removing the non alphabets
    for i in s:
        if i.isalpha():
            #Since this is Case insensitive
            s1 = s1 + i.lower()

    for j in s1:
        reverse = j + reverse
    if reverse == s1:
        return True
    return False