import copy

input_file = open('seat_layout.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines)
# print(len(input_lines))
for n, line in enumerate(input_lines):
    input_lines[n] = list(line)

height = len(input_lines)
width = len(input_lines[0])

run = 0
changes = True
while changes:
# while run < 5:
    print("Run",run)
    copy_il = copy.deepcopy(input_lines)
    cur_row = 0
    for n in copy_il:
        cur_index = 0
        for i in n:
            # print(cur_row,cur_index)
            adjacencies = []

            # UP SEAT
            if cur_row-1 >= 0:
                seat_up = copy_il[cur_row-1][cur_index]
                adjacencies.append(seat_up)

            # UP RIGHT SEAT
            if cur_row-1 >= 0 and cur_index+1 < width:
                seat_upright = copy_il[cur_row-1][cur_index+1]
                adjacencies.append(seat_upright)

            # RIGHT SEAT
            if cur_index+1 < width:
                seat_right = copy_il[cur_row][cur_index+1]
                adjacencies.append(seat_right)
            
            # DOWN RIGHT SEAT
            if cur_row+1 < height and cur_index+1 < width:
                seat_downright = copy_il[cur_row+1][cur_index+1]
                adjacencies.append(seat_downright)

            # DOWN SEAT
            if cur_row+1 < height:
                seat_down = copy_il[cur_row+1][cur_index]
                adjacencies.append(seat_down)
            
            # DOWN LEFT SEAT
            if cur_row+1 < height and cur_index-1 >= 0:
                seat_downleft = copy_il[cur_row+1][cur_index-1]
                adjacencies.append(seat_downleft)

            # LEFT SEAT
            if cur_index-1 >= 0:
                seat_left = copy_il[cur_row][cur_index-1]
                adjacencies.append(seat_left)
            
            # UP LEFT SEAT
            if cur_row-1 >= 0 and cur_index-1 >= 0:
                seat_upleft = copy_il[cur_row-1][cur_index-1]
                adjacencies.append(seat_upleft)

            
            # print(adjacencies,"\n")
            
            occupied = 0
            for a in adjacencies:
                if a == '#':
                    occupied += 1
                    
            if copy_il[cur_row][cur_index] == 'L' and occupied == 0:
                input_lines[cur_row][cur_index] = '#'
                
            if copy_il[cur_row][cur_index] == '#' and occupied >= 4:
                input_lines[cur_row][cur_index] = 'L'
            
            cur_index+=1    
        cur_row+=1

    if copy_il == input_lines:
        changes = False
    run += 1


# print(input_lines)
occupied = 0
for row in input_lines:
    for seat in row:
        if seat == '#':
            occupied += 1
            
print("There are",occupied,"occupied seats.")