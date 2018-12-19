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
  # "01234567890123456789012345"
  # "YYYY MM DD HH:mm:ss ±hh:mm"
  month = mon_to_num(date[7:10])
  month = '0' + str(month)
  month = month[-2:]
  ndatef = date[11:15] + '-' + month + '-' + date[4:6] + ' ' + date[16:]
  return ndatef

# Convert date to GMT and remove timezone.
def transposeDate(date):
    tz_delta = int(date[20:])
    time = int(date[11:13] + date[14:16])
    day = int(date[8:10])
    month = int(date[5:7])
    year = int(date[:4])

    gmt_time = time - tz_delta
    gmt_day = day
    gmt_month = month
    gmt_year = year

    if (gmt_time > 2359):
        gmt_day = day + 1
        gmt_time -= 2400
        if (gmt_day > daysinMonth(month, year)):
            gmt_month = month + 1
            gmt_day = 1
            if (gmt_month > 12):
                gmt_year = year + 1
                gmt_month = 1
    
    if (gmt_time < 0):
        gmt_day = day - 1
        gmt_time += 2400
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

    gmt_time = '0000' + str(gmt_time)
    gmt_time = gmt_time[-4:-2] + ':' + gmt_time[-2:]

    return str(gmt_year) + '-' + gmt_month + '-' + gmt_day + ' ' + gmt_time + date[16:19]

inp = str(input())

print(inp)

print("Cleaning date")
cd = cleanDate(inp)

print(cd)

print("Removing timezone...")

nd = transposeDate(cd)

print(nd)
