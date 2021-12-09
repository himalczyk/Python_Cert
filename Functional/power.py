def get_power(x: int, y: int) -> int:
    power = int(1)
    for i in range(y):
            power *= x
    return power

print(get_power(2,3))
print(get_power(0,3))
print(get_power(3,0))

