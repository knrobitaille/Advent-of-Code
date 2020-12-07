input_file = open('customs_answers.txt','r')
cust_lines = input_file.read().splitlines()
cust_lines.append('')
# print(cust_lines)


groups = {}
group_count = 0
person = 0
for i in cust_lines:
    if i == '':
        group_count += 1
        person = 0
    else:
        if not group_count in groups:
            groups[group_count] = {}
        groups[group_count][person] = i
        person += 1
        
# print(groups)
total_score = 0
for k,v in groups.items():
    this_groups_answers_list = []
    this_groups_answers_string = ''
    for k,v in v.items():
        this_groups_answers_list.append(v)
        this_groups_answers_string += v
    # print(this_groups_answers_list)
    # print(this_groups_answers_string)
    # print("set",(set(this_groups_answers_string)))
    
    score = len(set(this_groups_answers_string))
    for letter in set(this_groups_answers_string):
        for x in this_groups_answers_list:
            if letter not in x:
                score -= 1
                break
    total_score += score
    
print("Total score is",total_score)
    
    