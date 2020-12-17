input_data = [0,3,6]

num_said_dict = {}

turn = 1
while True:
    print("Turn",turn)
    if turn <= len(input_data):
        num = input_data[turn-1]
    else:
        num = next_num
    
    
    try:
        num_said_dict[num] += 1
    except:
        num_said_dict[num] = 1
    
    
    
    
    
    print("Number is",num)
    prev_num = num
    turn += 1
    if turn == 10:
        print("Finished.")
        break
    
    
    if num_said_dict[num] == 1:
        next_num = 0

print(num_said_dict)