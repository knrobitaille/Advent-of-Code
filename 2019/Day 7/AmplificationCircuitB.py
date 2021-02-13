input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

intcode = input_lines[0].split(',')

def intcode_comp(intcode,inputs,op=0):
    if len(inputs) == 2:
        phase = True
    else:
        phase = False
        
    if intcode[op] == '99':
            return None, None
        
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
            if phase:
                # print("Phase true",inputs[1])
                ask = inputs[1]
                phase = False
            else:
                # print("Phase false",inputs[0])
                ask = inputs[0]
            
            pos = int(intcode[op+1])
            # print(pos,ask)
            # print(len(intcode))
            intcode[pos] = ask
            op += 2
    
        elif opcode == '04':
            # print("Opcode 4")
            pos = int(intcode[op+1])
            value = intcode[pos]
            # print("Opcode 4:",value)
            op += 2
            return value, op
            
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
            
        if intcode[op] == '99':
            # print("99 found:",op,intcode[op])
            # print(intcode)
            return None, None

import copy

iterable = [5,6,7,8,9]
import itertools
all_combos = list(itertools.permutations(iterable,len(iterable)))
# print(all_combos)


highest = (0,[])
for combo in all_combos:
    # print("Combo",combo)
    A = copy.deepcopy(intcode)
    A_op = ''
    B = copy.deepcopy(intcode)
    B_op = ''
    C = copy.deepcopy(intcode)
    C_op = ''
    D = copy.deepcopy(intcode)
    D_op = ''
    E = copy.deepcopy(intcode)
    E_op = ''
    
    
    
    next_num = 0
    cur_highest = 0
    count = 0
    runs = 0
    while True:
        runs+=1
        # print("Amp",count,next_num)
        if count == 0:
            if A_op == '':
                next_num, A_op = intcode_comp(A,[next_num,combo[count]])
            else:
                next_num, A_op = intcode_comp(A,[next_num],A_op)
            
        elif count == 1:
            if B_op == '':
                next_num, B_op = intcode_comp(B,[next_num,combo[count]])
            else:
                next_num, B_op = intcode_comp(B,[next_num],B_op)
            
        elif count == 2:
            if C_op == '':
                next_num, C_op = intcode_comp(C,[next_num,combo[count]])
            else:
                next_num, C_op = intcode_comp(C,[next_num],C_op)
            
        elif count == 3:
            if D_op == '':
                next_num, D_op = intcode_comp(D,[next_num,combo[count]])
            else:
                next_num, D_op = intcode_comp(D,[next_num],D_op)
            
        elif count == 4:
            if E_op == '':
                next_num, E_op = intcode_comp(E,[next_num,combo[count]])
            else:
                next_num, E_op = intcode_comp(E,[next_num],E_op)
        
        
        # print("next_num",next_num)
        if next_num == None:
            break
        if count < 4:
            count += 1
        else:
            count = 0
        if next_num > cur_highest:
            cur_highest = next_num
            
            
    if cur_highest > highest[0]:
        highest=(cur_highest,combo)
    
print("Answer",highest[0])






























