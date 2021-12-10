with open ('Files/files/w1.txt', 'r') as file1, open ('Files/files/w2.txt', 'r', encoding='utf-8') as file2:
    listed_file1 = file1.readlines()
    listed_file2 = file2.readlines()
    two_files = zip(listed_file1, listed_file2)
    
with open ('Files/files/w3.txt', 'w', encoding='utf-8') as f_write:
    for line in two_files:
        f_write.writelines(line)
         
    # f_write.writelines(listed_file1)
    # f_write.writelines(listed_file2)
    