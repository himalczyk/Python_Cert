# DD/MM/YYYY

def day_index(year, month, day):
    z = year - 1 if month < 3 else year
    c = 0 if month < 3 else 2
    day_index = (int(23 * month / 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7 
    return day_index

def day_name(day_index):
    day_index_mapper =  ('Sun','Mon','Tue','Wed',"Thu",'Fri','Sat')
    print(f"Date: {day:02}.{month:02}.{year} - day - {day_index_mapper[day_index]}")


def get_day_name(date, sep = '-'): # format: YYYY-MM-dd
    year, month, day = date.split(sep)
    return int(year), int(month), int(day)


year, month, day = get_day_name(input("Provide date in format YYYY-MM-DD: \n"))
day_index = day_index(year, month, day)
day_name(day_index)

