def is_leap_year(year : int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def is_sunday(day : int, day_index : int) -> bool:
    return day == 0 and day_index == 6

months = [31,28,31,30,31,30,31,31,30,31,30,31]
days = [0,1,2,3,4,5,6]

start_year = 1900

sundays = 0
day_index = 0
current_month = 0

for year in range(0, 101):
    year += start_year
    if year < 1901:
        continue
    for month in months:
        if is_leap_year(year) and month == 28:
            month = 29
        for day in range(0, month):
            day_index += 1
            day_index = day_index % 7
            if is_sunday(day, day_index):
                sundays += 1
                #print("%d. %d. %d was a sunday" % (day +1, current_month +1, year))
        current_month += 1
        current_month = current_month % 12

print("There are %d sundays on the first day of a month between january first 1901 and dec 31 2000" % sundays)