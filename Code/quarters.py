months = ('Jan', 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

quarters = [month for month in months[::3]]

quarters_with_comma = "".join([month+", " for month in months[::3]])

print(quarters)
print(quarters_with_comma)