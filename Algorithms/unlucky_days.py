day = 13
year = int(input('Provide year: \n'))

fridays_13_in_year = 0
fridays_13_months = ""

for month in range(1, 13):
    z = year - 1 if month < 3 else year
    c = 0 if month < 3 else 2
    day_week_index = (int(23 * month / 9) + 13 + 4 + year + int(z / 4) - int(z / 100) + int(z / 400) - c) % 7
    # print(day_week[day_week_index])

    if day_week_index == 5:
        fridays_13_in_year += 1
        fridays_13_months += f"{month:02} "

    
print(f"Friday 13 count = {year}? {fridays_13_in_year} Friday 13s; Months: {fridays_13_months.split()}")
