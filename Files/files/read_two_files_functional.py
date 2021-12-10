def read_files(path1, path2):
    with open (path1, 'r') as file1, open (path2, 'r', encoding='utf-8') as file2:
        return file1.readlines(), file2.readlines()

def write_file(path, content):
    with open (path, 'w', encoding='utf-8') as f_write:
        f_write.writelines(content)
        
file1_content, file2_content = read_files('Files/files/w1.txt', 'Files/files/w3.txt')

write_file("new_file.txt", file1_content + ["\n\n"] + file2_content)
        
    # f_write.writelines(listed_file1)
    # f_write.writelines(listed_file2)
    