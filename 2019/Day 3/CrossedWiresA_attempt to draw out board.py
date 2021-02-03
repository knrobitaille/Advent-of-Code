input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

wire1 = input_lines[0].split(',')
wire2 = input_lines[1].split(',')

def process_wire(board,cur_spot,direction,distance,X_list):
    board = board.copy()
    if direction == "R":
        r_change = cur_spot[1]+distance
        for i in range(cur_spot[1]+1,r_change):
            if board[cur_spot[0]][i] == '.':
                board[cur_spot[0]][i] = '-'
            else:
                board[cur_spot[0]][i] = 'X'
                X_list.append((cur_spot[0],i))
        if board[cur_spot[0]][r_change] == '.':
            board[cur_spot[0]][r_change] = '+'
        else:
            board[cur_spot[0]][r_change] = 'X'
            X_list.append((cur_spot[0],r_change))
        cur_spot=(cur_spot[0],r_change)
        
    elif direction == "U":
        u_change = cur_spot[0]-distance
        for i in range(u_change+1,cur_spot[0]):
            if board[i][cur_spot[1]] == '.':
                board[i][cur_spot[1]] = '|'
            else:
                board[i][cur_spot[1]] = 'X'
                X_list.append((i,cur_spot[1]))
        if board[u_change][cur_spot[1]] == '.':
            board[u_change][cur_spot[1]] = '+'
        else:
            board[u_change][cur_spot[1]] = 'X'
            X_list.append((u_change,cur_spot[1]))
        cur_spot=(u_change,cur_spot[1])
        
    elif direction == "L":
        l_change = cur_spot[1]-distance
        for i in range(l_change+1,cur_spot[1]):
            if board[cur_spot[0]][i] == '.':
                board[cur_spot[0]][i] = '-'
            else:
                board[cur_spot[0]][i] = 'X'
                X_list.append((cur_spot[0],i))
        if board[cur_spot[0]][l_change] == '.':
            board[cur_spot[0]][l_change] = '+'
        else:
            board[cur_spot[0]][l_change] = 'X'
            X_list.append((cur_spot[0],l_change))
        cur_spot=(cur_spot[0],l_change)
        
    elif direction == "D":
        d_change = cur_spot[0]+distance
        for i in range(cur_spot[0]+1,d_change):
            if board[i][cur_spot[1]] == '.':
                board[i][cur_spot[1]] = '|'
            else:
                board[i][cur_spot[1]] = 'X'
                X_list.append((i,cur_spot[1]))
        if board[d_change][cur_spot[1]] == '.':
            board[d_change][cur_spot[1]] = '+'
        else:
            board[d_change][cur_spot[1]] = 'X'
            X_list.append(d_change,cur_spot[1])
        cur_spot=(d_change,cur_spot[1])
    return board, cur_spot, X_list

def print_board(board):
    for b in board:
        print(b)



wire1 = ['R8','U5','L5','D3']
wire2 = ['U7','R6','D4','L4']

# wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

# wire1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# wire2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

BOARD_SIZE = 11
board = []
for i in range(0,BOARD_SIZE):
    board.append(["."] * BOARD_SIZE)
    
coordA = coordB = int(BOARD_SIZE/2)
coordA = 9
coordB = 1
central_port = (coordA,coordB)
board[coordA][coordB] = 'o'

X_list = []
cur_spot = (coordA,coordB)
for inst in wire1:
    direction = inst[:1]
    distance = int(inst[1:])
    board, cur_spot, X_list = process_wire(board, cur_spot, direction, distance,X_list)

cur_spot = (coordA,coordB)
for inst in wire2:
    direction = inst[:1]
    distance = int(inst[1:])
    board, cur_spot, X_list = process_wire(board, cur_spot, direction, distance,X_list)

print_board(board)

lowest = ''
for n, i in enumerate(X_list):
    A = abs(X_list[n][0]-central_port[0])
    B = abs(X_list[n][1]-central_port[1])
    m_dist = A+B
    if lowest == '':
        lowest = m_dist
    elif m_dist < lowest:
        lowest = m_dist

print("Manhattan distance is",lowest)