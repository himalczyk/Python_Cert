import datetime

class YearException(Exception):
    def __init__(self):
        print("Year must be greated thatn 0 or lower than the current one. You cant be in the future")
        
class MonthException(Exception):
    def __init__(self):
        print("Month needs to be from 1-12")

while True:
    try:
        date = input("Type in date in YYYY-MM-dd format: \n")
        year, month, day = date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        if year < 0 or year > datetime.date.today().year:
            raise YearException
        if month not in range(1,13):
            raise MonthException
        # break else will not work
    except ValueError as e:
        print("Wrong format. Needs to be YYYY-MM-dd")
    except (YearException, MonthException):
        print("Wrong date validation")
    except Exception as e:
        print("Other error")
    else:
        print("after while loop, correct date")
        print(year, month, day)
        break
    
print("after the loop")
        


