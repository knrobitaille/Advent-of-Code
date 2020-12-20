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
        
print("Rules\n",rules)
print("Messages\n",messages)