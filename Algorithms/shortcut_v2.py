full_name = "United Nations Educational, Scientific and Cultural Organization"
# shortcut_comprehansion = "".join([word[0] for word in full_name.split() if word[0][0].isupper()])
# shortcut = ''.join(str(letter) for letter in shortcut_comprehansion)
    
print("".join([word[0] for word in full_name.split() if word[0].isupper()]))