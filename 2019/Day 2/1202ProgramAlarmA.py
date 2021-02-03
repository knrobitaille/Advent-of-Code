input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

input_lines = input_lines[0].split(',')

def process_opcode(opcode,first,second):
    if opcode == 1:
        # print("Opcode 1.")
        return first + second
    elif opcode == 2:
        # print("Opcode 2.")
        return first * second
    else:
        # print("Opcode is not 1,2, or 99. Error. Program terminating")
        return True

op = 0
for n in range(int(len(input_lines)//4)):
    opcode = int(input_lines[op])
    if opcode == 99:
        # print("\nOpcode 99. Program terminating")
        break    
    first_pos = int(input_lines[op+1])
    first_num = int(input_lines[first_pos])
    second_pos = int(input_lines[op+2])
    second_num = int(input_lines[second_pos])
    dest = int(input_lines[op+3])
    # print("\nOpcode",opcode)
    # print("First pos",first_pos,"=",first_num)
    # print("Second pos",second_pos,"=",second_num)
    # print("Destination",dest)

    processing = process_opcode(opcode,first_num,second_num)
    if processing == True:
        break
    else:
        input_lines[dest] = processing
    op += 4
    
print("Answer is",input_lines[0])