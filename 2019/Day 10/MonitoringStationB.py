input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

ast_map = [list(line) for line in input_lines]
WIDTH,HEIGHT = len(ast_map[0]),len(ast_map)

def find_all_asteroids(space_map):
    asteroids = []
    for r, row in enumerate(space_map):
        for c, col in enumerate(row):
            if col == '#':
                asteroids.append((c,r))
    return asteroids

asteroids = find_all_asteroids(ast_map)
# print("Asteroid locations\n",asteroids)

largest=('','')
for y in range(HEIGHT):
    for x in range(WIDTH):
        # print("\nChecking",x,y)
        if ast_map[y][x] == '.':
            continue
        slope_set = set()
        
        for a in asteroids:
            distance = (a[0]-x,a[1]-y)
            
            if distance == (0,0):
                continue
            elif distance[0] == 0:
                # print("up or down")
                if distance[1] > 0:
                    slope = 'down'
                else:
                    slope = 'up'
            elif distance[1] == 0:
                # print("right or left")
                if distance[0] > 0:
                    slope = 'right'
                else:
                    slope = 'left'
            else:
                add_dir = ''
                if x > a[0]:
                    add_dir='L'
                else:
                    add_dir='R'
                slope = str(round(distance[0]/distance[1],3))+add_dir
                
            # print(a,distance,slope)
            slope_set.add(slope)
            
        # print(slope_set)
        ast_map[y][x] = len(slope_set)
        if largest == ('',''):
            largest = ((x,y),len(slope_set))
        elif largest[1] < len(slope_set):
            largest = ((x,y),len(slope_set))
        
# print(largest)
station = largest[0]
# print(station)

import math

ast_deg_dis_dict = {}
ast_deg_dis_tups=[]
for asteroid in asteroids:
    if asteroid == station:
        continue
    else:
        x,y = (asteroid[0]-station[0]),(asteroid[1]-station[1])
        radians = math.atan2(x,y)
        degrees = math.degrees(radians)
        degrees = abs(degrees-180)
        distance = math.sqrt(x**2+y**2)
        # print(asteroid,degrees,distance)
        ast_deg_dis_dict[asteroid] = {'deg':degrees,"dis":distance}
        ast_deg_dis_tups.append((asteroid,degrees,distance))

# https://stackoverflow.com/questions/9376384/sort-a-list-of-tuples-depending-on-two-elements
ast_deg_dis_tups = sorted(ast_deg_dis_tups,key=lambda element: (element[1], element[2]))
# for i in ast_deg_dis_tups:
#     print(i)

import copy
ordered = []
while len(ast_deg_dis_tups) > 0:
    
    checking = copy.deepcopy(ast_deg_dis_tups)
    walker = 0
    
    to_delete = []
    while walker < len(checking):
        ordered.append(checking[walker])
        to_delete.append(walker)
        
        if len(checking) - walker == 1:
            break
        
        walker += 1
        try:
            while checking[walker-1][1] == checking[walker][1]:
                walker += 1
        except:
            pass
    
    for index in sorted(to_delete, reverse=True):
        del ast_deg_dis_tups[index]
        
# for n, item in enumerate(ordered):
#     print(n,item)

# print(ordered[199])
print("Answer",ordered[199][0][0]*100+ordered[199][0][1])
        
    
        
        
        
        
        
        
        
        