input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

input_lines = input_lines[0].split(',')

def process_opcode12(opcode,first,second):
    if opcode == '01':
        # print("Opcode 1.")
        return first + second
    elif opcode == '02':
        # print("Opcode 2.")
        return first * second
    else:
        # print("Opcode is not 1,2, or 99. Error. Program terminating")
        return True

op = 0
for n in range(int(len(input_lines)//4)):
    opcode_instr = str(input_lines[op]).zfill(5)
    opcode = opcode_instr[3:]
    if opcode == '99':
        # print("\nOpcode 99. Program terminating")
        break  
    elif opcode in ['01','02']:
        param1mode = int(opcode_instr[2:3])
        param2mode = int(opcode_instr[1:2])
        param3mode = int(opcode_instr[:1])
        
        if param1mode == 0:
            first_pos = int(input_lines[op+1])
            first_num = int(input_lines[first_pos])
        else:
            first_num = int(input_lines[op+1])
        
        if param2mode == 0:
            second_pos = int(input_lines[op+2])
            second_num = int(input_lines[second_pos])
        else:
            second_num = int(input_lines[op+2])
        dest = int(input_lines[op+3])
        
        input_lines[dest]=process_opcode12(opcode,first_num,second_num)
    
    elif opcode in ['03','04']:
        if opcode == '03':
            ask = input("Enter for opcode 3: ")
            pos = int(input_lines[op+1])
            input_lines[pos] = ask

        if opcode == '04':
            pos = int(input_lines[op+1])
            value = input_lines[pos]
            print("Opcode 4:",value)
        
    
    if opcode in ['03','04']:
        op+=2
    else:
        op+=4


