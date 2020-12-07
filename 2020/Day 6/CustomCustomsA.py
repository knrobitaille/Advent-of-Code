input_file = open('customs_answers.txt','r')
cust_lines = input_file.read().splitlines()
cust_lines.append('')
# print(cust_lines)

groups = []
cur_group = ''
for line in cust_lines:
    if line == "":
        # print("Group's combined answers were:",cur_group)
        groups.append(cur_group)
        cur_group = ''
    cur_group += line
    
group_sum = 0
for group in groups:
    group_sum += len(set(group))
    # print("Group was",group,"so score was",len(set(group)))
    
print("Total score was",group_sum)