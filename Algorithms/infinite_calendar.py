from math import floor

day = int(input('Provide day [1..31]: \n'))
month = int(input('Provide month [1..12]: \n'))
year = int(input('Provide year: \n'))
z = year
c = 2

if month < 3:
    z = year - 1
    c = 0
    
calculate_day_of_the_week = (int(23*month/9) + day + 4 + year + int(z/4) - int(z/100) + int(z/400) - c) %7

day_of_the_week = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
    
print(f"Date: {day}{month}{year} = {day_of_the_week[calculate_day_of_the_week]}")
