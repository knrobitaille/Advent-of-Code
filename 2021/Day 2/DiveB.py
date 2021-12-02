input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
print(input_lines)
# print(len(input_lines))


hor = 0
depth = 0
aim = 0

for i in input_lines:
    x = i.split(" ")
    
    if x[0] == 'forward':
        hor += int(x[1])
        depth += int(x[1])*aim
    if x[0] == 'up':
        aim -= int(x[1])
        # depth -= int(x[1])
    if x[0] == 'down':
        aim += int(x[1])
        # depth += int(x[1])
        
        
    
    # print(hor,depth,aim)

print(hor,depth,aim)
print(hor*depth)
