unesco = "United Nations Educational, Scientific and Cultural Organization"
splitted_unesco = unesco.split(" ")
short_unesco = ''

for word in splitted_unesco:
    if word[0][0].isupper():
        short_unesco = short_unesco + word[0][0]
    
print(f"Created shortcut: {short_unesco}")