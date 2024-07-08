def timeConversion(s):
    period = s[-2:]
    hour, minute, second = s[0:-2].split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    mil_hour = hour + 12
    if hour < 12 and period == 'AM':
        mil_hour = hour
    elif hour > 24:
        mil_hour -= 12
    if hour == 12 and period == 'PM':
        mil_hour = hour
    elif hour == 12 and period == 'AM':
        mil_hour = 0
    return f'{mil_hour:02}:{minute:02}:{second:02}'