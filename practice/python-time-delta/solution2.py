#!/bin/python3

# https://www.hackerrank.com/challenges/python-time-delta/problem

import math
import os
import random
import re
import sys

# Set export OUTPUT_PATH=PATH
# OUTPUT_PATH = '/Users/aschwinschilperoort/Programming/Github/Hackerrank/practice/python-time-delta/output.txt'

# Complete the time_delta function below.

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

def daysinMonth(month, year):
    if (month == 2):
        if (isleapYear(year)):
            return 29
        else:
            return 28
    elif (month in [1,3,5,7,8,10,12]):
        return 31
    else:
        return 30

# Clean the date format:
def cleanDate(date):
  # new dateformat
  # "0123456789012345678901234"
  # "YYYY MM DD HH:mm:ss ±hhmm"
  month = mon_to_num(date[7:10])
  month = '0' + str(month)
  month = month[-2:]
  ndatef = date[11:15] + '-' + month + '-' + date[4:6] + ' ' + date[16:]
  return ndatef

def transposeDate(date):
    tz_minute = date[23:25]
    tz_hour = date[21:23]
    tz_sign = date[20]

    minute = int(date[14:16])
    hour = int(date[11:13])
    day = int(date[8:10])
    month = int(date[5:7])
    year = int(date[:4])

    gmt_minute = minute
    gmt_hour = hour
    gmt_day = day
    gmt_month = month
    gmt_year = year

    gmt_minute = minute - int(tz_sign + tz_minute)

    if (gmt_minute > 59):
      gmt_hour += 1
      gmt_minute -= 60

    if (gmt_minute < 0):
      gmt_hour -= 1
      gmt_minute += 60

    gmt_hour = gmt_hour - int(tz_sign + tz_hour)

    if (gmt_hour > 23):
        gmt_day = day + 1
        gmt_hour -= 24
        if (gmt_day > daysinMonth(month, year)):
            gmt_month = month + 1
            gmt_day = 1
            if (gmt_month > 12):
                gmt_year = year + 1
                gmt_month = 1
    
    if (gmt_hour < 0):
        gmt_day = day - 1
        gmt_hour += 24
        if (gmt_day < 1):
            gmt_month -= 1
            gmt_day = daysinMonth((gmt_month - 1 + 12) % 12 + 1, year)
            if (gmt_month == 0):
                gmt_year -= 1
                gmt_month = 12

    gmt_month = '0' + str(gmt_month)
    gmt_month = gmt_month[-2:]

    gmt_day = '0' + str(gmt_day)
    gmt_day = gmt_day[-2:]

    gmt_hour = '0' + str(gmt_hour)
    gmt_hour = gmt_hour[-2:]

    gmt_minute = '0' + str(gmt_minute)
    gmt_minute = gmt_minute[-2:]

    return str(gmt_year) + '-' + gmt_month + '-' + gmt_day + ' ' + gmt_hour + ':' + gmt_minute + date[16:19]

def time_delta(date1, date2):
    cd1 = cleanDate(date1)
    cd1 = transposeDate(cd1)

    cd2 = cleanDate(date2)
    cd2 = transposeDate(cd2)

    print('\n')
    print(cd1)
    print(cd2)

    return cd1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
