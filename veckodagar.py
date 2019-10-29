year = int(input("Year: "))
while year not in range (1538,9999):
    print("Out of allowed range 1583 to 9999")
    year = int(input("Year: " ))



month = int(input("Month: "))
while month not in range (1,13):
    print("Out of allowed range 1 to 12")
    month = int(input("Month: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    day = int(input("Day: "))
    while day not in range (1,32):
        print("Out of allowed range 1 to 31")
        day = int(input("Day: "))
elif month in [4, 6, 9, 11]:
    day = int(input("Day: "))
    while day not in range (1,31):
        print("Out of allowed range 1 to 30")
        day = int(input("Day: "))
elif month == 2:
    if (year%4==0 and year%100!=0 or year%400==0):
        day = int(input("Day: "))
        while day not in range (1,30):
            print("Out of allowed range 1 to 29")
            day = int(input("Day: "))
    else:
        day = int(input("Day: "))
        while day not in range (1,29):
            print("Out of allowed range 1 to 28")
            day = int(input("Day: "))

if month == 1 or month == 2:
    month += 12
    year -= 1

weekday = ( day + 13*(month+1)//5 + year + year//4
 - year//100 + year//400 ) % 7

if weekday == 0:
    print("It is a saturday")
if weekday == 1:
    print("It is a sunday")
if weekday == 2:
    print("It is a monday")
if weekday == 3:
    print("It is a tuesday")
if weekday == 4:
    print("It is a wednesday")
if weekday == 5:
    print("It is a thursday")
if weekday == 6:
    print("It is a friday")
