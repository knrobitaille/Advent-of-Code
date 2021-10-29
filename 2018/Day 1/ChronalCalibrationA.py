input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)


freq = 0

for i in input_lines:
    
    sign = i[0]
    num = int(i[1:])
    
    if sign == '+':
        freq += num
    elif sign == '-':
        freq -= num
        
    else:
        print("Check input")
        
print("Frequency is",freq)