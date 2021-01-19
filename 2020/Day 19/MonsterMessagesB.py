input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

rules = []
messages = []

switch = False

for i in input_lines:
    if i == '':
        switch = True
        continue
    if switch:
        messages.append(i)
    else:
        rules.append(i)
        
rules_dict = {}
for rule in rules:
    rulesplit = rule.split(':')
    key = int(rulesplit[0])
    rules_dict[key] = []
    rulesplit = rulesplit[1].split("|") 
    for rule in rulesplit:
        value = []
        for r in rule.strip().split():
            try:
                value.append(int(r))
            except:
                value.append(r.strip('""'))
        
        rules_dict[key].append(value)
   
# print("Rules\n",rules)
# print("Rules\n",rules_dict)
for k, v in rules_dict.items():
    print(k,v)
print("Messages\n",messages)
print()

seen_rules = {}

def solve1(rule_num):
    """
    I was on the right track on my own but I referred to this video
    to help me get over the hump:
        https://www.youtube.com/watch?v=dgnK4ASzVPU
    """

    options = rules_dict[rule_num]
    
    if ['a'] in options:
        return['a']
    elif ['b'] in options:
        return['b']
    elif rule_num in seen_rules:
        return seen_rules[rule_num]
    
    possible = []
    for option in options:
        ops = []
        for rule in option:
            subop = solve1(rule)
        
            if len(ops) == 0:
                ops = subop.copy()
            else:
                combined = []
                for r in subop:
                    for op in ops:
                        combined.append(op+r)
                ops = combined.copy()
        possible += ops
        
    seen_rules[rule_num] = possible
    return possible

all_possible = solve1(0)

all_possible_set = set()
for poss in all_possible:
    all_possible_set.add(poss)
    
count = 0
for msg in messages:
    if msg in all_possible_set:
        count+=1
        
print(count)
