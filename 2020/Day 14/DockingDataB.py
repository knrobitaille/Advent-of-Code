input_file = open('init_prog.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines,'\n')

#
# Solved part A when Day 14 first came out, but resolved 01/26/2021 to make it cleaner.
# This was to help me more easily figure out part 2 below!
#

def apply_mask_to_value(mask,value):
    length = len(mask) # should be 36
    bin_value = bin(int(value))[2:].rjust(length,'0')
    masked_val = ''
    for i in range(length):
        if mask[i] == 'X':
            masked_val += bin_value[i]
        else:
            masked_val += mask[i]
    return masked_val

def apply_mask_to_key(mask,key):
    length = len(mask) # should be 36
    key = key.split(']')[0].split('[')[1]
    bin_key = bin(int(key))[2:].rjust(length,'0')
    masked_key = ''
    for i in range(length):
        if mask[i] == '0':
            masked_key += bin_key[i]
        elif mask[i] == '1':
            masked_key += mask[i]
        elif mask[i] == 'X':
            masked_key += 'X'
    return masked_key

def get_key_combos(masked_key):
    combinations = 2 ** masked_key.count('X')
    combos = []
    for n in range(combinations):
        combos.append((bin(n)[2:].zfill(masked_key.count('X'))))
    key_combos = []
    for combo in combos:
        count = 0
        new_key = ''
        for i in masked_key:
            if i != 'X':
                new_key += i
            else:
                new_key += combo[count]
                count += 1
        key_combos.append(new_key)
    return key_combos
            
memory = {}
cur_mask = ''
for line in input_lines:
    if 'mask' in line:
        cur_mask = line.split(" = ")[1]
        continue
    else:
        key = line.split(" = ")[0]
        value = line.split(" = ")[1]    
        masked_key = apply_mask_to_key(cur_mask,key)
        key_combos = get_key_combos(masked_key)
        for k in key_combos:
            memory[int(k,2)]=int(value)
 
answer = 0
for k,v in memory.items():
    answer += v
print("The answer is",answer)