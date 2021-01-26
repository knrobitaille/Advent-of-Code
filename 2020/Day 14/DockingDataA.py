input_file = open('init_prog.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines,'\n')

#
# Solved this back when Day 14 came out, but resolved 01/26/2021 to make it cleaner.
# This was to help me to figure out part 2 more easily (which I did not solve previously)
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

memory = {}
cur_mask = ''
for line in input_lines:
    if 'mask' in line:
        cur_mask = line.split(" = ")[1]
        continue
    else:
        key = line.split(" = ")[0]
        value = line.split(" = ")[1]        
        masked_val = apply_mask_to_value(cur_mask,value)
        memory[key] = masked_val
        
answer = 0
for k,v in memory.items():
    answer += int(v,2)
print("The answer is",answer)