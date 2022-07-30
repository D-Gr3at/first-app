import datetime

# %a - Weekday, short version
# %A - Weekday, full version
# %w - Weekday as a number 0-6, 0 is Sunday
# %d - Day of month 01-31
# %b - Month name, short version
# %B - Month name, full version
# %m - Month as a number 01-12
# %y - Year, short version, without century
# %Y - Year, full version
# %H - Hour 00-23
# %I - Hour 00-12
# %p - AM/PM
# %M - Minute 00-59
# %S - Second 00-59
# %Z - Timezone
# %z - UTC offset


if __name__ == '__main__':
    dt = datetime.datetime.now()
    # dd/mm/yyyy
    print(dt.strftime("%d/%m/%Y"))

    # dd-mm-yyyy
    print(dt.strftime("%d-%m-%Y"))

    # wed 20, July 2022
    print(dt.strftime("%a %d, %B %Y"))

    # time
    print(dt.strftime("%I:%M:%S %p"))

    #  datetime
    print(dt.strftime("%a %d, %B %Y. %I:%M:%S %p"))
