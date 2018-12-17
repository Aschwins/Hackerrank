#!/bin/python3

# https://www.hackerrank.com/challenges/python-time-delta/problem

import math
import os
import random
import re
import sys

# Set export $OUTPUT_PATH = PATH
# OUTPUT_PATH = '/Users/aschwinschilperoort/Programming/Github/Hackerrank/practice/python-time-delta/output.txt'

# Complete the time_delta function below.

# This function calculates if a year is a leap year. (Leapyears etc.)
def isleapYear(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
       return False

def get_tz_diff(str1, str2):
    diff = int(str1)-int(str2)
    if (diff < 0):
        diff = diff * -1
        real_diff = -1* (int(diff / 100) * 60 * 60 + diff % 100 * 60)
    else:
        real_diff = int(diff / 100) * 60 * 60 + diff % 100 * 60
    return real_diff

# This function counts the amount of leap years between to given years
def countleapYears(year1, year2):
    count = 0
    if (year2 > year1):
        for i in range(year1, year2):
            if isleapYear(i):
                count += 1
        return count
    else:
        for i in range(year2, year1):
            if isleapYear(i):
                count += 1
        return count

def mon_to_num(string):
    if string == 'Jan':
        return 1
    if string == 'Feb':
        return 2
    if string == 'Mar':
        return 3
    if string == 'Apr':
        return 4
    if string == 'May':
        return 5
    if string == 'Jun':
        return 6
    if string == 'Jul':
        return 7
    if string == 'Aug':
        return 8
    if string == 'Sep':
        return 9
    if string == 'Oct':
        return 10
    if string == 'Nov':
        return 11
    if string == 'Dec':
        return 12

# function that gives the amount of days in a month (no leapyear)
def monthtoDays(month):
    if (month in [1,3,5,7,8,10,12]):
        return 31
    elif (month == 2):
        return 28
    else:
        return 30

# function that gives the difference in days between two given months
def monthdiffinDays(month1, month2):
    days = 0
    if (month2 > month1):
        for i in range(month1, month2):
            days += monthtoDays(i)
        return days
    else:
        for i in range(month2, month1):
            days += monthtoDays(i)
        return days

def time_delta(t1, t2):
    print("\n")
    n_leapyears = countleapYears(int(t1[11:15]), int(t2[11:15]))
    d_years = (int(t1[11:15]) - int(t2[11:15])) * 365 * 24 * 60 * 60 + n_leapyears * 24 * 60 * 60
    print("Year difference in seconds: %s"%d_years)

    # Check if the month difference contains a leapday.
    if (int(t1[11:15]) < int(t2[11:15])):
        if (isleapYear(int(t2[11:15])) & (mon_to_num(t1[7:10]) <=2) & (mon_to_num(t2[7:10]) >= 3)):
            leapday = 1
        else:
            leapday = 0
    else:
        if (isleapYear(int(t1[11:15])) & (mon_to_num(t2[7:10]) <=2) & (mon_to_num(t1[7:10]) >= 3)):
            leapday = 1
        else:
            leapday = 0

    d_months = (monthdiffinDays(mon_to_num(t1[7:10]),mon_to_num(t2[7:10]))) * 24 * 60 * 60 + leapday * 24 * 60 * 60
    print("Month difference in seconds: %s"%d_months)

    d_days = (int(t1[4:6]) - int(t2[4:6])) * 24 * 60 * 60
    print("Day difference in seconds: %s"%d_days)

    d_hours = (int(t1[16:18]) - int(t2[16:18])) * 60 * 60
    print("Hour difference in seconds: %s"%d_hours)

    d_minutes = (int(t1[19:21]) - int(t2[19:21])) * 60
    print("Minute difference in seconds: %s"%d_minutes)

    d_seconds = int(t1[22:24]) - int(t1[22:24])
    print("Second difference in seconds: %s"%d_seconds)

    d_timezone = get_tz_diff(t1[26:], t2[26:])
    print("Timezone difference in seconds: %s" %d_timezone)

    t_delta = abs(d_timezone + d_seconds + d_minutes + d_hours + d_days + d_months + d_years)
    t_delta = str(t_delta)
    return t_delta
    #Day dd Mon yyyy hh:mm:ss +xxxx
    #012345678901234567890123456789

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()