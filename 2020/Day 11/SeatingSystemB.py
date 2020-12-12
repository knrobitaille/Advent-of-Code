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

            # UP SEAT - n
            move = 1
            while (cur_row-move) >= 0:
                if copy_il[cur_row-move][cur_index] == ".":
                    move += 1
                else:
                    seat_up = copy_il[cur_row-move][cur_index]
                    adjacencies.append(seat_up)
                    break


            # UP RIGHT SEAT - +
            move = 1
            while (cur_row-move) >= 0 and (cur_index+move) < width:
                if copy_il[cur_row-move][cur_index+move] == ".":
                    move += 1
                else:
                    seat_upright = copy_il[cur_row-move][cur_index+move]
                    adjacencies.append(seat_upright)
                    break


            # RIGHT SEAT n +
            move = 1
            while (cur_index+move) < width:
                if copy_il[cur_row][cur_index+move] == ".":
                    move += 1
                else:
                    seat_right = copy_il[cur_row][cur_index+move]
                    adjacencies.append(seat_right)
                    break
            
            
            # DOWN RIGHT SEAT + +
            move = 1
            while (cur_row+move) < height and (cur_index+move) < width:
                if copy_il[cur_row+move][cur_index+move] == ".":
                    move += 1
                else:
                    seat_downright = copy_il[cur_row+move][cur_index+move]
                    adjacencies.append(seat_downright)
                    break


            # DOWN SEAT + n
            move = 1
            while (cur_row+move) < height:
                if copy_il[cur_row+move][cur_index] == ".":
                    move += 1
                else:
                    seat_down = copy_il[cur_row+move][cur_index]
                    adjacencies.append(seat_down)
                    break
            
            
            # DOWN LEFT SEAT + -
            move = 1
            while (cur_row+move) < height and (cur_index-move) >= 0:
                if copy_il[cur_row+move][cur_index-move] == ".":
                    move += 1
                else:
                    seat_downleft = copy_il[cur_row+move][cur_index-move]
                    adjacencies.append(seat_downleft)
                    break    


            # LEFT SEAT n -
            move = 1
            while (cur_index-move) >= 0:
                if copy_il[cur_row][cur_index-move] == ".":
                    move += 1
                else:
                    seat_left = copy_il[cur_row][cur_index-move]
                    adjacencies.append(seat_left)
                    break    
            
            
            # UP LEFT SEAT - -
            move = 1
            while (cur_row-move) >= 0 and (cur_index-move) >= 0:
                if copy_il[cur_row-move][cur_index-move] == ".":
                    move += 1
                else:
                    seat_upleft = copy_il[cur_row-move][cur_index-move]
                    adjacencies.append(seat_upleft)
                    break    

            
            
            # if cur_row == 0 and cur_index == 6:
            #     print(adjacencies,"\n")
            
            occupied = 0
            for a in adjacencies:
                if a == '#':
                    occupied += 1
                    
            if copy_il[cur_row][cur_index] == 'L' and occupied == 0:
                input_lines[cur_row][cur_index] = '#'
                
            if copy_il[cur_row][cur_index] == '#' and occupied >= 5:
                input_lines[cur_row][cur_index] = 'L'
            
            cur_index+=1    
        cur_row+=1
        
    # for line in input_lines:
    #     print(line)
        
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