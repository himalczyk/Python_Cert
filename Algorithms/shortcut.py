full_name = "United Nations Educational, Scientific and Cultural Organization"
splitted_full_name = full_name.split(" ")
shortcut = ''

for word in splitted_full_name:
    if word[0][0].isupper():
        shortcut = shortcut + word[0][0]
    
print(f"Created shortcut: {shortcut}")