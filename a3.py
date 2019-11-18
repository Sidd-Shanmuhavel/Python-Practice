# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:10:06 2019

@author: Siddhartha Shanmuhavel

Student Id: 119220393
"""
'''This program is to print the calendar of any valid given month and year
between 2000 and 2099 both inclusive, without using any inbuilt date functions'''

# This function returns the no. of days in that month
def num_days(month, year):
    no_of_days = 0
    if month in (1, 3, 5, 7, 8, 10, 12):
        no_of_days = 31
    elif month in (4, 6, 9, 11):
        no_of_days = 30
    else:
        if year % 4 == 0:
            no_of_days = 29
        else:
            no_of_days = 28
    return no_of_days

#This function returns the next date
def next_day(d, m, y):
    if d < num_days(m, y):
        return d + 1, m, y
    else:
        if m < 12:
            return 1, m + 1, y
        return 1, 1, y + 1

''' This function returns the day on which
the first of that month falls '''
def start_day(month, year):
    d = 1
    m = 1
    y = 2000
    start_date = 6
    while  m != month or y != year:
        d, m, y = next_day(d, m, y)
        if start_date < 6:
            start_date = start_date + 1
        else:
            start_date = 0
    return start_date

''' Takes month and year as input and prints
its calendar ''' 
def cal(month, year):
    if (year > 1999 and year < 2100) and (month <=12 and month >1):
        start_d = start_day(month, year)
        num_of_days = num_days(month, year)
        ''' flag1 is to start printing exactly
        on the day when 1 falls and flag2 is
        print only until the no. of days the month has.'''
        flag1 = 0
        flag2 = 1
        print("Su Mo Tu We Th Fr Sa")
        for i in range(1,8):
            for j in range(1,8):
                if flag1 == start_d:
                    if flag2 <= num_of_days:
                        print("%2d " %flag2, end="")
                        flag2 = flag2 + 1
                else:
                    print("   ", end="")
                    flag1 = flag1 + 1
            print("")
    else:
        print("Incorrect input for Month or Year received..!!")
    
    