input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))
def get_coords(cur_spot,direction,distance,coord_list):
    coord_list = coord_list.copy()
    if direction == 'R':
        r_change = cur_spot[1]+distance
        for i in range(cur_spot[1]+1,r_change+1):
            coord_list.append((cur_spot[0],i))
        cur_spot = (cur_spot[0],r_change)
    elif direction == 'U':
        u_change = cur_spot[0]+distance
        for i in range(cur_spot[0]+1,u_change+1):
            coord_list.append((i,cur_spot[1]))
        cur_spot = (u_change,cur_spot[1])
    elif direction == 'L':
        l_change = cur_spot[1]-distance
        for i in range(l_change,cur_spot[1]):
            coord_list.append((cur_spot[0],i))
        cur_spot = (cur_spot[0],l_change)
    elif direction == 'D':
        d_change = cur_spot[0]-distance
        for i in range(d_change,cur_spot[0]):
            coord_list.append((i,cur_spot[1]))
        cur_spot = (d_change,cur_spot[1])
    return cur_spot, coord_list

wire1 = input_lines[0].split(',')
wire2 = input_lines[1].split(',')

### Examples
# wire1 = ['R8','U5','L5','D3']
# wire2 = ['U7','R6','D4','L4']

# wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

# wire1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# wire2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

coordA = coordB = 0
central_port = (coordA,coordB)

wire1_coords = []
cur_spot = central_port
for inst in wire1:
    direction = inst[:1]
    distance = int(inst[1:])
    cur_spot,wire1_coords = get_coords(cur_spot,direction,distance,wire1_coords)
    
wire2_coords = []
cur_spot = central_port
for inst in wire2:
    direction = inst[:1]
    distance = int(inst[1:])
    cur_spot,wire2_coords = get_coords(cur_spot,direction,distance,wire2_coords)

intersection = set(wire1_coords) & set(wire2_coords)
lowest = ''
for intersect in intersection:
    m_dist = abs(intersect[0])+abs(intersect[1])
    if lowest == '' or m_dist < lowest:
        lowest = m_dist
print("Answer",lowest)