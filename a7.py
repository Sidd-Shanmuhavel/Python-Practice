# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 01:13:15 2019

@author: Siddhartha

@Id number: 119220393
"""

def most_common(text, n):
    splitlist = []
    listofwords = []
    
    for char in text:
        if char.isalpha() == False:
            text = text.replace(char," ")
    
    splitlist = text.lower().split()
    
    for word in splitlist:
        if splitlist.count(word) >= n and word not in listofwords:
            listofwords.append(word)
    
    return sorted(listofwords)

print(most_common("'Meow,' s-aid the cat's cat.s",2))

print(most_common(" “Here is our captain, and he will not allow you to perish on the open sea.” "+
                  "On perceiving me, the stranger addressed me in English, although with a foreign "+
                  "accent. “Before I come on board your vessel,” said he, “will you have the kindness to "+
                  "inform me whither you are bound?” ",3))