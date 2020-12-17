input_data = [6,4,12,1,20,0,16]

num_said_dict = {}

#
# This takes a bit to run.
#

turn = 1
while True:
    
    if turn % 1000 == 0: 
        print("Turn",turn)
        
    if turn <= len(input_data):
        num = input_data[turn-1]
    else:
        num = next_num
    
    try:
        num_said_dict[num]["count"] += 1
        num_said_dict[num]["turns"].append(turn)
    except:
        num_said_dict[num] = {'count':1,'turns':[turn]}
    

    if turn == 30000001:
        print("Number is",num)
        
    if turn % 1000 == 0:  
        print("Number is",num)
        
    prev_num = num
    turn += 1

    
    if num_said_dict[num] == 1:
        next_num = 0
    else:
        # do this

        most_rec_turn = num_said_dict[num]["turns"][len(num_said_dict[num]["turns"])-1]
        second_most_rec_turn = num_said_dict[num]["turns"][len(num_said_dict[num]["turns"])-2]
        next_num = most_rec_turn - second_most_rec_turn

    if turn == 30000001:
        print("Finished.")
        break


# print(num_said_dict)