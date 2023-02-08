def leap_year(year):
    """return if given year is a leap year"""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


year = [3, 12, 100, 400]
for i in range(len(year)):
    if leap_year(year[i]):
        print(f"{year[i]} is a leap year")
    else:
        print(f"{year[i]} not a leap year")