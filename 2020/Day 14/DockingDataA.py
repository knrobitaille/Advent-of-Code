input_file = open('init_prog.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines)
# print(len(input_lines))

memory = {}

cur_mask = 'X' * 36
for line in input_lines:
    # print('\n')
    inst = line.split('=')[0].strip()
    value = line.split('=')[1].strip()
    # print(inst,value)    
    
    if 'mask' in inst:
        cur_mask = value
        continue
    else:
        key = inst.split(']')[0].split('[')[1]
        # print("key",key)
        
        bin_value = bin(int(value))[2:]
        bin_value = bin_value.rjust(36,'0')
        
        # print("Bin value",bin_value)
        
        masked_val = ''
        
        for i in range(36):
            # print('Checking',i)
            # print("Starting with",masked_val)
            if cur_mask[i] == 'X':
                masked_val += str(bin_value)[i]
            else:
                masked_val += cur_mask[i]
        
    # print("Masked_val",masked_val)
    memory[key] = int(masked_val,2)
        

answer = 0
for k,v in memory.items():
    answer += v
    
print("The answer is",answer)