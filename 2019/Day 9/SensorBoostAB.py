input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

intcode = input_lines[0].split(',')

### Tests ###
# intcode = ['109', '-1', '4', '1', '99'] # outputs -1
# intcode = ['109', '-1', '104', '1', '99'] # outputs 1
# intcode = ['109', '-1', '204', '1', '99'] # outputs 109
# intcode = ['109', '1', '9', '2', '204', '-6', '99'] # outputs 204
# intcode = ['109', '1', '109', '9', '204', '-6', '99'] # outputs 204
# intcode = ['109', '1', '209', '-1', '204', '-106', '99'] # outputs 204
# intcode = ['109', '1', '3', '3', '204', '2', '99'] # outputs the input
# intcode = ['109', '1', '203', '2', '204', '2', '99'] # outputs the input
# print(intcode)


ADD_SPACES = 10000
for i in range(ADD_SPACES):
    intcode.append('0')
op = 0
relative_base = 0

while intcode[op] != '99':
    opcode_instr = str(intcode[op]).zfill(5)
    opcode = opcode_instr[3:]
    # print(opcode_instr)
    # print()
    # print("Opcode",opcode)
    # print("Relative base",relative_base)
    
    param1mode = int(opcode_instr[2:3])
    param2mode = int(opcode_instr[1:2])
    param3mode = int(opcode_instr[:1])
    
    if opcode not in ['03','04','09']:
        
        if param1mode == 0:
            first_pos = int(intcode[op+1])
            first_num = int(intcode[first_pos])
        elif param1mode == 1:
            first_num = int(intcode[op+1])
        elif param1mode == 2:
            first_num = int(intcode[relative_base + int(intcode[op+1])])
        
        if param2mode == 0:
            second_pos = int(intcode[op+2])
            second_num = int(intcode[second_pos])
        elif param2mode == 1:
            second_num = int(intcode[op+2])
        elif param2mode == 2:
            second_num = int(intcode[relative_base + int(intcode[op+2])])
            
            
            
        if param3mode == 0:
            dest = int(intcode[op+3])
        elif param3mode == 1:
            dest = int(intcode[op+3])
            dest = op+3
        elif param3mode == 2:
            dest = relative_base + int(intcode[op+3])        
    
    if opcode == '01':
        # print("Opcode 1")
        intcode[dest] = first_num+second_num
        op += 4

    elif opcode == '02':
        # print("Opcode 2")
        intcode[dest] = first_num*second_num
        op += 4

    elif opcode == '03':
        # print("Opcode 3")
        ask = input("Enter for opcode 3: ")
        
        if param1mode == 0:
            pos = int(intcode[op+1])
        elif param1mode == 1:
            pos = int(intcode[op+1])
        elif param1mode == 2:
            pos = int(relative_base + int(intcode[op+1]))
        intcode[pos] = ask
        op += 2

    elif opcode == '04':
        # print("Opcode 4")
        
        if param1mode == 0:
            pos = int(intcode[op+1])
            value = intcode[pos]
        elif param1mode == 1:
            value = int(intcode[op+1])
        elif param1mode == 2:
            value = int(intcode[relative_base + int(intcode[op+1])])
        print("Opcode 4:",value)
        op += 2
        
    elif opcode == '05':
        # print("Opcode 5")
        if first_num != 0:
            op = second_num
        else:
            op+=3

    elif opcode == '06':
        # print("Opcode 6")
        if first_num == 0:
            op = second_num
        else:
            op+=3
        
    elif opcode == '07':
        # print("Opcode 7")
        if first_num < second_num:
            intcode[dest] = 1
        else:
            intcode[dest] = 0
        op += 4

    elif opcode == '08':
        # print("Opcode 8")
        if first_num == second_num:
            intcode[dest] = 1
        else:
            intcode[dest] = 0
        op += 4
        
    elif opcode == '09':
        # print("Opcode 9")
        if param1mode == 0:
            pos = int(intcode[op+1])
            relative_base += int(intcode[pos])
        elif param1mode == 1:
            relative_base += int(intcode[op+1])
        elif param1mode == 2:
            relative_base += int(intcode[relative_base + int(intcode[op+1])])
        op += 2

# print()
# print(intcode)