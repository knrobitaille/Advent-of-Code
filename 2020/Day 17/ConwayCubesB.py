input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
"""
If a cube is active and exactly 2 or 3 of its neighbors are also active,
    the cube remains active. Otherwise, the cube becomes inactive.
    
If a cube is inactive but exactly 3 of its neighbors are active, the cube
    becomes active. Otherwise, the cube remains inactive.
"""
def find_neighbors(cube,cube_dict,dim=4):
    x = cube[0]
    y = cube[1]
    z = cube[2]
    w = cube[3]
    neighbors = []
    for xa in range(x-1,x+2):
        for ya in range(y-1,y+2):
            for za in range(z-1,z+2):
                for wa in range(w-1,w+2):
                    if x == xa and y == ya and z == za and w == wa:
                        continue
                    try:
                        neighbors.append(cube_dict[xa,ya,za,wa])
                    except:
                        pass
    return neighbors

def switch_cube(cube,cube_dict):
    if cube_dict[cube] == '.':
        cube_dict[cube] = '#'
    else:
        cube_dict[cube] = '.'
    return cube_dict

def check_switch(cube_value,neighbors):
        if cube_value == '#':
            if neighbors.count('#') < 2 or neighbors.count('#') > 3:
                return True
        if cube_value == '.':
            if neighbors.count('#') == 3:
                return True
            
def expand_matrix(scope,cube_dict,dim=4):
    for x in range(-scope,scope+1):
        for y in range(-scope,scope+1):
            for z in range(-scope,scope+1):
                for w in range(-scope,scope+1):
                    if (x,y,z,w) not in cube_dict:
                        cube_dict[x,y,z,w] = '.'
    return cube_dict

def create_initial_cube_dict(input_lines):
    cube_dict = {}
    size = int(len(input_lines[0])/2)
    for n, line in enumerate(input_lines):
        for c in range(-size,size+1):
            try:
                cube_dict[c,n-size,0,0]=line[c+size]
            except:
                pass
    return cube_dict, size
                
#####################################################
cube_dict, size = create_initial_cube_dict(input_lines)       
CYCLES = 6
scope = size
for c in range(CYCLES):
    scope+=1
    expand_matrix(scope,cube_dict)
    
    to_switch = []
    for k,v in cube_dict.items():
        neighbors = find_neighbors(k,cube_dict)
        if check_switch(v, neighbors):
            to_switch.append(k)
        
    for cube in to_switch:
        cube_dict = switch_cube(cube,cube_dict)
        
active_count = 0
for k,v in cube_dict.items():
    if v == '#':
        active_count += 1
print("Answer is",active_count)