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
        
print(largest)
# for row in ast_map:
#     print(row)
                