input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

input_lines = input_lines[0].split(',')

def process_opcode(opcode,first,second):
    if opcode == 1:
        return first + second
    elif opcode == 2:
        return first * second
    else:
        return True

def process_input(input_list):
    input_lines = input_list.copy()
    op = 0
    for n in range(int(len(input_lines)//4)):
        opcode = int(input_lines[op])
        if opcode == 99:
            break   
        first_pos = int(input_lines[op+1])
        first_num = int(input_lines[first_pos])
        second_pos = int(input_lines[op+2])
        second_num = int(input_lines[second_pos])
        dest = int(input_lines[op+3])
        processing = process_opcode(opcode,first_num,second_num)
        if processing == True:
            break
        else:
            input_lines[dest] = processing
        op += 4
    return input_lines[0]

noun = 0
verb = 0
for i in range(100):
    verb = 0
    found = False
    for n in range(100):
        input_lines[1]=noun
        input_lines[2]=verb
        answer = process_input(input_lines)
        if answer == 19690720:
            found = True
            break
        verb += 1
    if found:
        break
    noun += 1

print("Answer:",100*noun+verb)

