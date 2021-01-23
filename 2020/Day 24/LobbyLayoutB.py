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
# print(tiles)

from collections import Counter
c = Counter(tiles)

all_tiles = {}
for k,v in c.items():
    if v%2 != 0:
        all_tiles[k]='b'
    else:
        all_tiles[k]='w'
# print(all_tiles)

def extend_all_tiles(all_tiles):
    farthest_tile_max = max(all_tiles)
    if farthest_tile_max[0]>farthest_tile_max[1]:
        farthest_tile_max = farthest_tile_max[0]
    else:
        farthest_tile_max = farthest_tile_max[1]
    farthest_tile_min = min(all_tiles)
    if farthest_tile_min[0]>farthest_tile_min[1]:
        farthest_tile_min = farthest_tile_min[0]
    else:
        farthest_tile_min = farthest_tile_min[1]
    distance = max([abs(farthest_tile_max),abs(farthest_tile_min)])+1
    for i in range(distance+1):
        for j in range(distance+1):
            if (i,j) not in all_tiles:
                all_tiles[(i,j)]='w'
            if (-i,j) not in all_tiles:
                all_tiles[(-i,j)]='w'
            if (i,-j) not in all_tiles:
                all_tiles[(i,-j)]='w'
            if (-i,-j) not in all_tiles:
                all_tiles[(-i,-j)]='w'

extend_all_tiles(all_tiles) 
def check_adjacencies(tile,tile_dict):
    try:
        e=tile_dict[(tile[0]+0,tile[1]+1)]
    except:
        e='w'
    try:
        se=tile_dict[(tile[0]+1,tile[1]+1)]
    except:
        se='w'
    try:
        sw=tile_dict[(tile[0]+1,tile[1]+0)]
    except:
        sw='w'
    try:
        w=tile_dict[(tile[0]+0,tile[1]-1)]
    except:
        w='w'
    try:
        nw=tile_dict[(tile[0]-1,tile[1]-1)]
    except:
        nw='w'
    try:
        ne=tile_dict[(tile[0]-1,tile[1]+0)]
    except:
        ne='w'
    adj = [e,se,sw,w,nw,ne]
    return adj
    

DAYS = 100
for d in range(DAYS):
    # print("Day",d+1)
    extend_all_tiles(all_tiles) 
    to_flip = []
    for tile in all_tiles:
        adj = check_adjacencies(tile,all_tiles)
        if all_tiles[tile] == 'w':
            if adj.count('b') == 2:
                to_flip.append(tile)
        if all_tiles[tile] == 'b':
            if adj.count('b') == 0 or adj.count('b') > 2:
                to_flip.append(tile)
    for tile in to_flip:
        if all_tiles[tile]=='b':
            all_tiles[tile]='w'
        else:
            all_tiles[tile]='b'
    if d == DAYS-1:
        black_tiles = 0
        for tile in all_tiles:
            if all_tiles[tile]=='b':
                black_tiles += 1
        print("Black tiles on Day",DAYS,"=",black_tiles,'\n')