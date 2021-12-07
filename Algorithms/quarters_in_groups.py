months = ('Jan', 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

quarters = [month for month in months[::3]]

quarters_with_comma = "".join([month+", " for month in months[::3]])

quarter_lenght = 3

# list comprehansions to achieve result

quarters_with_separation = [[month for index, month in enumerate(months) if index//quarter_lenght == quarter] for quarter in range(4)]

quarters2 = []

# standard loops iteration over lists to achieve result

for quarter in range(4):
    quart = []
    for index, month in enumerate(months):
        if index // quarter_lenght == quarter:
            quart.append(month)
    quarters2.append(quart)

print(quarters)
print(quarters_with_comma)
print(quarters_with_separation)
print(quarters2)