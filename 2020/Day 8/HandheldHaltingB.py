from copy import deepcopy

input_file = open('boot_code.txt','r')
instructions = input_file.read().splitlines()
# print(instructions)
# print(len(instructions))




for index, line in enumerate(instructions):
    test_instructions = deepcopy(instructions)
    # print(index,line)
    if 'nop' in line:
        # print('nop in line')
        # print(test_instructions[index])
        test_instructions[index] = line.replace('nop', 'jmp')
        # print(test_instructions[index])
    elif 'jmp' in line:
        # print('jmp in line')
        # print(test_instructions[index])
        test_instructions[index] = line.replace('jmp', 'nop')
    #     print(test_instructions[index])
    # print(index,line,'\n')
    
    accumulator = 0
    count = 0
    n = 0
    visited = []
    
    while True:
        if n >= len(test_instructions):
            print("test_instructions complete.")
            print("accumulator",accumulator)
            break
        if n not in visited:
            visited.append(n)
        else:
            # print("already visited", n)
            # print("accumulator",accumulator)
            break
        count += 1
        # print("\ncount",count)
        # print('n',n)
        command = test_instructions[n].split()[0]
        sign = test_instructions[n].split()[1][:1]
        amount = test_instructions[n].split()[1][1:]
        # print(command,sign,amount)
        
        if command == "acc":
            n += 1
            if sign == '+':
                accumulator += int(amount)
            else:
                accumulator -= int(amount)
                
        if command == "nop":
            n += 1
            pass
        
        if command == "jmp":
            if sign == '+':
                n += int(amount)
            else:
                n -= int(amount)
                
    
        if count > 10000:
            print("This is likely an infinite loop...")
            break
        
    # print("accumulator",accumulator)
    
    