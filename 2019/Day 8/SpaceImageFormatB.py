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
        
answer = [i for i in range(WIDTH*HEIGHT)]
for i in range(WIDTH*HEIGHT):
    layer = 1
    while True:
        if layers[layer][i] != '2':
            answer[i] = layers[layer][i]
            break
        else:
            layer += 1
            
answer_two = []
cur_row = ''
for i in answer:
    if i == '1':
        cur_row += '#'
    else:
        cur_row += '-'
    if len(cur_row) == WIDTH:
        answer_two.append(cur_row)
        cur_row = ''
for i in answer_two:
    print(i)