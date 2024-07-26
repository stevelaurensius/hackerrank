def dayOfProgrammer(year):
    leap = False
    if year > 1918:
        if year % 400 == 0:
            leap = True
        elif year % 4 == 0 and year % 100 != 0:
            leap = True
    elif year < 1918:
        if year % 4 == 0:
            leap = True
        else:
            leap = False
    elif year == 1918:
        return f'26.09.{year}'

    if not leap:
        return f'13.09.{year}'
    elif leap:
        return f'12.09.{year}'
