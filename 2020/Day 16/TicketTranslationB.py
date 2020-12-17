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

rules = {}

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
        cur_range = []
        for i in range(first_range_min,first_range_max+1):
            valid_nums.append(i)
            cur_range.append(i)
        for i in range(second_range_min,second_range_max+1):
            valid_nums.append(i)
            cur_range.append(i)
        key = line.split(':')[0]
        rules[key] = set(cur_range)
        
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
valid_tickets = []

for ticket in nearby_tickets:
    valid = True
    for num in ticket:
        if int(num) not in valid_nums:
            valid = False
            invalid_nums.append(int(num))
            invalid_count += 1
    if valid:
        valid_tickets.append(ticket)
        
# print("Valid tickets remaining",valid_tickets)
# print("Rules",rules)

answer_dict = {}
for i in range(TICKET_FIELDS):
    answer_dict[i] = set(rules.keys())
# print("\nAnswer_dict",answer_dict)



for ticket in valid_tickets:
    # print("\n\nChecking ticket",ticket)
    
    for i, n in enumerate(ticket):
        # print("\nindex", i, "number",n)
        
        
        to_remove = []
        for rule in answer_dict[i]:
            # print(rule)
            if int(n) not in rules[rule]:
                # print(n,"not in",rule,rules[rule])
                to_remove.append(rule)
        #remove
        for rule in to_remove:
            # print("Remove",rule,"from",i)
            answer_dict[i].remove(rule)

print(answer_dict)

seen = set()
for value in sorted(answer_dict.values(),key=len):
    value -= seen
    seen |= value

print(your_ticket)
departure_vals = []
for k,v in answer_dict.items():
    print(k,v)
    if 'departure' in str(v):
        departure_vals.append(int(your_ticket[k]))

print(departure_vals)
answer = 1
for i in departure_vals:
    answer *= i
print("Answer",answer)

