input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

class Tiles:
    def __init__(self,id_num,tile):
        self.id_num = id_num
        self.tile = tile
        
        self.top = tile[0]
        self.bottom = tile[9]
        self.left = ''
        self.right = ''
        for line in self.tile:
            self.left += line[0]
            self.right += line[9]
            
        self.edges = [self.top,self.bottom,self.left,self.right]

all_tiles = []
cur_id = 0
cur_tile = []
for line in input_lines:
    if line == "":
        continue
    elif "Tile" in line:
        cur_id = line.split()[1].strip(":")
    else:
        cur_tile.append(line)
        if len(cur_tile) == 10:
            finished_tile = Tiles(cur_id,cur_tile)
            all_tiles.append(finished_tile)
            cur_tile = []

all_edges = []
for tile in all_tiles:
    # print()
    # print("Tile",tile.id_num)
    # # print(tile.tile)
    # print("T",tile.top)
    # print("B",tile.bottom)
    # print("L",tile.left)
    # print("R",tile.right)
    all_edges.append(tile.top)
    all_edges.append(tile.top[::-1])
    all_edges.append(tile.bottom)
    all_edges.append(tile.bottom[::-1])
    all_edges.append(tile.left)
    all_edges.append(tile.left[::-1])
    all_edges.append(tile.right)
    all_edges.append(tile.right[::-1])
    
# print(all_edges)

### Need to find four corner tiles which would be tiles that have two edges
### which don't match anyone else. Easy. (I think)
### Update... not easy because of flipping and rotating
### Final update, okay it wasn't too hard
    
from collections import Counter
c = Counter(all_edges)
# print(c)

corners = []
for tile in all_tiles:
    edge_count = 0
    for edge in tile.edges:
        if c[edge] == 2 or c[edge[::-1]] == 2:
            # print(tile.id_num,edge)
            edge_count += 1
    if edge_count == 2:
        corners.append(tile.id_num)
        
# print("Four corners are",corners)
        
answer = 1
for corner in corners:
    answer *= int(corner)
print("Answer is",answer)

    