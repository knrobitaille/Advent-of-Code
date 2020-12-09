input_file = open('boot_code.txt','r')
instructions = input_file.read().splitlines()
print(instructions)
print(len(instructions))



accumulator = 0
jumps = 0
No_OPeration = 0

count = 0
n = 0
visited = []

while True:
    if n >= len(instructions):
        print("Instructions complete.")
        break
    if n not in visited:
        visited.append(n)
    else:
        print("already visited", n)
        print("accumulator",accumulator)
        break
    count += 1
    print("\ncount",count)
    print('n',n)
    command = instructions[n].split()[0]
    sign = instructions[n].split()[1][:1]
    amount = instructions[n].split()[1][1:]
    print(command,sign,amount)
    
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
    
    