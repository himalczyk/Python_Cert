# with open ('Files/files/w1.txt', 'r') as file1:
#     for line in file1:
#         print(line.strip()) #strip deletes white characters
        
# with open ('Files/files/w2.txt', 'r', encoding='utf-8') as file1:
#     for line in file1:
#         print(line.strip()) #strip deletes white characters

with open ('Files/files/w1.txt', 'r') as file1, open ('Files/files/w2.txt', 'r', encoding='utf-8') as file2:
    listed_file1 = file1.readlines()
    listed_file2 = file2.readlines()
longer = listed_file1
smaller = listed_file2
if len(listed_file1) < len(listed_file2):
    longer = listed_file2
    smaller = listed_file1
for index, line in enumerate(longer):
    print(line.strip())
    if index < len(smaller):
        print(smaller[index].strip())
