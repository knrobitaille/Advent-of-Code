input_file = open('ticket_info.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines)
# print(len(input_lines))

TICKET_FIELDS = 20

your_ticket = []
your_ticket_check = False
nearby_tickets = []
valid_nums = []
for line in input_lines:
    
    # print(line)
    
    if " or " in line:        
        first_range = line.split(' or ')[0].split(':')[1].strip()
        second_range = line.split(' or ')[1].strip()
        # print(first_range,second_range)
        first_range_min = int(first_range.split('-')[0])
        first_range_max = int(first_range.split('-')[1])
        second_range_min = int(second_range.split('-')[0])
        second_range_max = int(second_range.split('-')[1])
        # print(first_range_min,first_range_max)
        # print(second_range_min,second_range_max)
        for i in range(first_range_min,first_range_max+1):
            valid_nums.append(i)
        for i in range(second_range_min,second_range_max+1):
            valid_nums.append(i)
        
    if line.count(',') == TICKET_FIELDS-1:
        if not your_ticket_check:
            nums = line.split(",")
            your_ticket = nums
            your_ticket_check = True
        else:
            nums = line.split(",")
            nearby_tickets.append(nums)
            
valid_nums = set(valid_nums)
# print("Valid numbers set",valid_nums)

# print("Your ticket",your_ticket)
# print("Nearby tickets",nearby_tickets)

invalid_count = 0
invalid_nums = []

for ticket in nearby_tickets:
    valid = True
    for num in ticket:
        if int(num) not in valid_nums:
            valid = False
            invalid_nums.append(int(num))
            invalid_count += 1
            
# print("Invalid ticket count",invalid_count)
# print("Invalid nums",invalid_nums)
print("Answer is",sum(invalid_nums))

        