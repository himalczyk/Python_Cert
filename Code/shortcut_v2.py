full_name = "United Nations Educational, Scientific and Cultural Organization"
shortcut = ''

for word in full_name.split(" "):
    if word[0][0].isupper():
        shortcut = shortcut + word[0][0]
    
print(f"Created shortcut: {shortcut}")