from math import hypot

# N 4, W 1, S 6, E 5
position = [0, 0]

while True:
    get_direction = input("Provide direction and step:")

    if not get_direction:
        print(f"Calculated position: {position}.")
        print(round(hypot(position[0], position[1]), 2))
        break
    splitted_direction = get_direction.split(" ")
    direction = splitted_direction[0]
    step = int(splitted_direction[1])

    if direction.upper() == 'N':
        position[1] += step
    if direction.upper() == 'S':
        position[1] -= step
    if direction.upper() == 'W':
        position[0] -= step
    if direction.upper() == 'E':
        position[0] += step
        
        