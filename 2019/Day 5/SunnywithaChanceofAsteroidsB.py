input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

intcode = input_lines[0].split(',')

op = 0
while intcode[op] != '99':
    opcode_instr = str(intcode[op]).zfill(5)
    opcode = opcode_instr[3:]
    # print("Opcode",opcode)
    
    if opcode not in ['03','04']:
        param1mode = int(opcode_instr[2:3])
        param2mode = int(opcode_instr[1:2])
        param3mode = int(opcode_instr[:1])
        
        if param1mode == 0:
            first_pos = int(intcode[op+1])
            first_num = int(intcode[first_pos])
        else:
            first_num = int(intcode[op+1])
        
        if param2mode == 0:
            second_pos = int(intcode[op+2])
            second_num = int(intcode[second_pos])
        else:
            second_num = int(intcode[op+2])
        dest = int(intcode[op+3])
    
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
        pos = int(intcode[op+1])
        intcode[pos] = ask
        op += 2

    elif opcode == '04':
        # print("Opcode 4")
        pos = int(intcode[op+1])
        value = intcode[pos]
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

# print(intcode)