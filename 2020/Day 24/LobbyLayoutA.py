input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

directions = []
current_direction = []
for line in input_lines:
    count = 0
    while True:
        if count >= len(line):
            break
        if line[count] in ['n','s']:
            current_direction.append(line[count:count+2])
            count += 2
        else:
            current_direction.append(line[count])
            count += 1
    directions.append(current_direction)
    current_direction = []      
# print(directions)
    
direction_dict = {'e':(0,1),'se':(1,1),'sw':(1,0),'w':(0,-1),'nw':(-1,-1),'ne':(-1,0)}
tiles = []
for direction in directions:
    # print(direction,"\n")
    coord = (0,0)
    for d in direction:
        coord = (coord[0]+direction_dict[d][0],coord[1]+direction_dict[d][1])
    tiles.append(coord)    
    
print(tiles)

from collections import Counter
c = Counter(tiles)

black_tiles = 0
for k,v in c.items():
    if v%2 != 0:
        black_tiles += 1
print("The answer is",black_tiles)
        