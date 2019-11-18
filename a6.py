# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:15:43 2019

@author: Siddhartha Shanmuhavel

@id: 119220393
"""


''' This function takes a positive integer value and returns a 
string containing the number expressed in English words '''
def to_engish(number):
    if number > 0 and number // 1000 == 0:
        n0 = number // 100
        n1 = (number // 10) % 10
        n2 = (number % 10)

        hundredsplace = ""
        tensplace = ""
        unitsplace = ""
    
        l1 = ['one','two','three','four','five','six','seven','eight','nine']
        l2 = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
        l3 = ['ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety','']
        
        if n1 == 1:
            if n2 != 0:
                tensplace = l2[n2 - 1]
            else:
                tensplace = l3[0]
        else:
            if n2 != 0:
                tensplace = l3[n1 - 1]
                if tensplace == "":
                    unitsplace = l1[n2 - 1]
                else:
                    unitsplace = '-' + l1[n2 - 1]
            else:
                tensplace = l3[n1 - 1]
        #Checking Hundreds place
        if n0 != 0:
            if tensplace == "" and unitsplace == "":
                hundredsplace = l1[n0 - 1] + " hundred"
            else:
                hundredsplace = l1[n0 - 1] + " hundred and "
    
        numberinwords = hundredsplace + tensplace + unitsplace 
        return numberinwords
    else:
        return "Please enter a positive integer less than 1000"

    
#This function checks if two given strings are Anagrams or not
def anagrams(s1, s2):
    dict1 = {}
    dict2 = {}
    
    #Storing the characters as keys of the dictonary
    for i in s1:
        if i.isalpha():
            #Since this is Case insensitive
            if i.lower() not in dict1:
                dict1[i.lower()] = 1
            else:
                dict1[i.lower()] = dict1[i.lower()] + 1
                
    for i in s2:
        if i.isalpha():
            #Since this is Case insensitive
            if i.lower() not in dict2:
                dict2[i.lower()] = 1
            else:
                dict2[i.lower()] = dict2[i.lower()] + 1
    
    if dict1 == dict2:
        return True
    return False