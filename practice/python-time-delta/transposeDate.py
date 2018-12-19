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

# Convert date to GMT and remove timezone. OLD SOLUTION (DOESNT PROPErLy work)
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