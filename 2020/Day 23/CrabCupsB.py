input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
print(input_lines)
# print(len(input_lines))

#
# Got stumped on part 2 and used this person solution to help figure it out
# https://gist.github.com/rendyanthony/05863f6211eef180c795542796a92b42
#

cups = [int(i) for i in input_lines[0]] # list comprehension baby!
TOTAL_CUPS = 1000000
for n in range(10,TOTAL_CUPS+1):
    cups.append(n)
    
# print(cups)

cycle_dict = dict(zip(cups, cups[1:]))
cycle_dict[cups[-1]] = cups[0]
# print(cycle_dict)

MOVES = 10000000
PICKUP_QUANTITY = 3

for n in range(MOVES):
    if n % 100000 == 0:
        print(round(n/MOVES,2))
    # print("\nMove",n+1)
    # print(cycle_dict)
    if n == 0:
        select = cups[0]
    else:
        select = next_cup
    # print("Selected",select)

    pick_quanitity = 3
    pickup = [cycle_dict[select]]
    for i in range(PICKUP_QUANTITY-1):
        pickup.append(cycle_dict[pickup[-1]])
    # print("Pickup",pickup)
        
    place = select - 1
    while place in pickup or place == 0:
        place -= 1
        if place <= 0:
            place = max(cups)
    # print("Place",place)
    
    # selected cup now points to what the last picked up cup pointed to
    cycle_dict[select] = cycle_dict[pickup[-1]]
    # last picked up cup now points to what the destination/placement cup pointed to
    cycle_dict[pickup[-1]] = cycle_dict[place]
    # the destination/placement cup now points to the first cup that was picked up
    cycle_dict[place] = pickup[0]
    
    # the next cup will be what the selected cup is now pointing to
    next_cup = cycle_dict[select]
    
# print("Final dict",cycle_dict)
num1 = cycle_dict[1]
num2 = cycle_dict[num1]
print(num1,num2,num1*num2)