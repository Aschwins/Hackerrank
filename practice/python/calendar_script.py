import calendar

year, month, day = list(map(int, input().split()))

wd = calendar.weekday(year, month, day)

result = list(calendar.day_name)[wd]

print(result.upper())