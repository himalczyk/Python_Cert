def get_even(digit):
    return digit % 2 == 0 and digit != 0

digits = range(10)
# f = filter(get_even, digits)
# # print(*f)

#decimal to binary
def dec_to_bin(digit):
    return bin(digit)

after_filtering = list(filter(dec_to_bin, digits))
print(after_filtering)
after_filtering_mapping = map(dec_to_bin, after_filtering)
print(after_filtering_mapping)

def sorting_by_name_and_gender(name):
    return name[-1].lower() == 'a', name

example = [2,2,3,4,5,6,7,8,8,6,6,9,9,2,3,4]
name = ["Ala","Ela","Jan","Adam","Ada"]
print(sorted(example))
print(sorted(name, reverse=True))
print(sorted(name, key = sorting_by_name_and_gender))