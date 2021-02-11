input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

WIDTH = 25
HEIGHT = 6



layers = {}
layer = 1
cur_row = ''
zero_count = 0
lowest = ''
for i in input_lines[0]:
    if i == '0':
        zero_count+=1
    cur_row += i
    
    if len(cur_row) == WIDTH*HEIGHT:
        if lowest == '':
            lowest = (layer,zero_count)
        elif lowest[1] > zero_count:
            lowest = (layer,zero_count)
        layers[layer] = cur_row
        cur_row = ''
        layer += 1
        zero_count = 0
        
ones = 0
twos = 0
for i in layers[lowest[0]]:
    if i == '1':
        ones += 1
    elif i == '2':
        twos += 1
        
print("Answer",ones*twos)