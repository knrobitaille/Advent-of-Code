input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

#
# This code works but it is UGLY
# need to work on solving better / using functions
#

cups = [int(i) for i in input_lines[0]] # list comprehension baby!
MOVES = 100

for n in range(MOVES):
    
    # print("\nMove",n+1)
    # print("Cups",cups)
    
    if n == 0:
        selected_cup = cups[0]
    else:
        if prev_index+1 >= len(cups):
            prev_index = -1
        selected_cup = cups[prev_index+1]
    cur_index = cups.index(selected_cup)
    # print("select",selected_cup)
    
    start = 0
    indices_take = []
    for i in range(3):
        take = i+1+cur_index
        if take >= len(cups):
            take = 0
            if 0 in indices_take:
                take = 1
                if 1 in indices_take:
                    take = 2
        indices_take.append(take)
      
    pickup_three = []
    for i in indices_take:
        pickup_three.append(cups[i])
        
    for i in pickup_three:
        del_index = cups.index(i)
        # print("Del",cups[del_index])
        del cups[del_index]
    
    # print("pick up",pickup_three)
    # print("Cups",cups)
   
    found = False
    dest = selected_cup-1
    while not found:
        try:
            dest_index = cups.index(dest)
            found = True
        except:
            dest -= 1
            if dest < 0:
                dest = max(cups)
            
    # print("dest",dest)
    dest_index += 1
    for i in range((len(pickup_three))):
        cups.insert(dest_index+i,pickup_three[i])
    
    prev_cup = selected_cup
    prev_index = cups.index(prev_cup)
    
# print(cups)
before_1 = []
after_1 = []
found_1 = False
for i in cups:
    if i == 1:
        found_1 = True
        continue
    if found_1:
        after_1.append(str(i))
    else:
        before_1.append(str(i))
        
answer = after_1+before_1
# print(answer)

answer = ''.join(answer)
print(answer)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    