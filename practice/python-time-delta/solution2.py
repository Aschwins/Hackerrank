#!/bin/python3

# https://www.hackerrank.com/challenges/python-time-delta/problem

import math
import os
import random
import re
import sys

# Set export OUTPUT_PATH=PATH
# OUTPUT_PATH='/Users/aschwinschilperoort/Programming/Github/Hackerrank/practice/python-time-delta/output.txt'

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

def daysinYear(year):
    if (isleapYear(year)):
        return 366
    else:
        return 365

def time_delta(date1, date2):

    # first we get a cleandate (cd)
    cd1 = cleanDate(date1)
    cd1 = transposeDate(cd1)

    cd2 = cleanDate(date2)
    cd2 = transposeDate(cd2)

    # We use the lexographical order characteristic of strings to find out what the biggest date is
    # Let bd be the biggest date and sd be the smallest date
    if cd1 > cd2:
        bd = cd1
        sd = cd2
    elif cd2 > cd1:
        bd = cd2
        sd = cd1
    else:
        return str(0)

    #print("Biggest date converted to GMT: %s" %bd)
    #print("Smallest date converted to GMT: %s" %sd)


    # Once we have the biggest date we can deduct!
    bd_hour = int(bd[11:13])
    bd_minute = int(bd[14:16])
    bd_second = int(bd[17:])
    sd_hour = int(sd[11:13])
    sd_minute = int(sd[14:16])
    sd_second = int(sd[17:])
    bd_year = int(bd[:4])
    bd_month = int(bd[5:7])
    bd_day = int(bd[8:10])
    sd_year = int(sd[:4])
    sd_month = int(sd[5:7])
    sd_day = int(sd[8:10])

    # Hoeveel seconden hebben we nog over in de dag van de kleinste dag?
    if ((bd_year != sd_year) | (bd_month != sd_month) | (sd_day != bd_day)):
        rsd = 86400 - sd_hour * 60 * 60 - sd_minute * 60 - sd_second
    else:
        rsd = 0
        print("Over in kleinste dag: %s"%rsd)

    # Hoeveel dagen hebben we nog over in de maand van de kleinste dag?
    if ((bd_year != sd_year) | (bd_month != sd_month)):
        rdm = daysinMonth(sd_month, sd_year) - sd_day
        if (rdm < 0):
            rdm = 0
    else:
        rdm = 0
    #print("Dagen over in de kleinste maand: %s"%rdm)

    # Hoeveel dagen hebben we nog over in het jaar van de kleinste dag?
    if ((bd_year != sd_year)):
        rdy = 0
        for i in range(sd_month + 1, 12 + 1):
            rdy += daysinMonth(i, sd_year)
    else:
        rdy = 0
    #print("Dagen over tot het einde van het jaar: %s"%rdy)
    
    # Hoeveel jaren moeten we overbruggen tot het jaar van de grootste datum?
    dy = 0
    for i in range(sd_year + 1, bd_year):
        dy += daysinYear(i)
    #print("Jaren in dagen te overbruggen tot het laatste jaar: %s"%dy)
    
    # Hoeveel maanden moeten we overbruggen tot de maand van de grootste datum?
    dm = 0
    if ((bd_year != sd_year)):
        for i in range(1, bd_month):
            dm += daysinMonth(i, bd_year)
    else:
        for i in range(sd_month + 1, bd_month):
            dm += daysinMonth(i, sd_year)
    #print("Maanden in dagen te overbruggen tot de laatste maand: %s"%dm)

    dd = 0
    if ((bd_year != sd_year) | (bd_month != sd_month)):
        dd = bd_day -  1
    else:
        for i in range(sd_day + 1, bd_day):
            dd += 1
    #print("Aantal dagen in grootste datum: %s"%dd)

    # Hoeveel seconden zitten er nog in de laatste dag?
    if ((bd_year != sd_year) | (bd_month != sd_month) | (bd_day != sd_day)):
        rsd2 = bd_hour * 60 * 60 + bd_minute * 60 + bd_second
    else:
        rsd2 = (bd_hour - sd_hour) * 60 * 60 + (bd_minute - sd_minute) * 60 + (bd_second - sd_second) 
    #print("Aantal seconden nog in de laatste dag: %s"%rsd2)

    return str(rsd + rdm * 24 * 60 * 60 + rdy * 24 * 60 * 60 + dy * 24 * 60 * 60 + dm * 24 * 60 * 60 + dd * 24 * 60 * 60 + rsd2)

    # d_hour = bd_hour - sd_hour
    # d_minute = bd_minute - sd_minute
    # d_second = bd_second - sd_second

    # d_day = dayDiff(sd, bd)

    # return str(d_day * 24 * 60 * 60 + d_hour * 60 * 60 + d_minute * 60 + d_second * 60)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
