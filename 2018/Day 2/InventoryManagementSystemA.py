input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)

two_count = 0
three_count = 0

for i in input_lines:
    # print(i)
    two_check = False
    three_check = False
    for k in i:
        # print(k)
        if i.count(k) == 2:
            two_check = True
        if i.count(k) == 3:
            three_check = True
            
    if two_check == True:
        # print('2')
        two_count += 1
    if three_check == True:
        # print('3')
        three_count += 1
        
print("2:", two_count)
print("3:", three_count)
print("Answer:", two_count*three_count)