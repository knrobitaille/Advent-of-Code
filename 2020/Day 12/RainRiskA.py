input_file = open('nav_instructions.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines)
# print(len(input_lines))


north = 0
south = 0
east = 0
west = 0

cur_dir = 90

# value_sum = 0
for i in input_lines:
    command = i[:1]
    value = int(i[1:])
    # value_sum += value
    
    if command == 'N':
        north += value
    if command == 'S':
        south += value
    if command == 'E':
        east += value
    if command == 'W':
        west += value
    
    if command == 'F':
        if cur_dir == 0:
            north += value
        elif cur_dir == 180:
            south += value
        elif cur_dir == 90:
            east += value
        elif cur_dir == 270:
            west += value
            
    if command == 'L':
        cur_dir -= value
        if cur_dir < 0:
            cur_dir += 360
    if command == 'R':
        cur_dir += value
        if cur_dir >= 360:
            cur_dir -= 360
    
# print(value_sum)    
# print("North",north)
# print("South",south)
# print("East",east)
# print("West",west)

n_s = north-south
e_w = east-west

print("The answer is",abs(n_s)+abs(e_w))