input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)

import itertools

freq = 0
freq_list = []
n=0
print("This takes a couple of minutes...")
for i in itertools.cycle(input_lines):
    if n %50000 == 0:
        print("Pass",n)
    n+=1
    
    sign = i[0]
    num = int(i[1:])
    
    if sign == '+':
        freq += num
    elif sign == '-':
        freq -= num
        
    else:
        print("Check input")
    
    if freq in freq_list:
        break
    else:
        freq_list.append(freq)
        
print("Frequency is",freq)
print("This took",n,"passes")