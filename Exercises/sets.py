s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])

print("sum", s1 | s2)
print("same values", s1 & s2)
print("subtraction", s1 - s2)
print("subtraction", s2 - s1)
print("symmetric difference", s1 | s2)
