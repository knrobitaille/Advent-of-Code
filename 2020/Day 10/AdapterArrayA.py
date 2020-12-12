input_file = open('jolt_adapters.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines)

input_lines.append('0') # add charging outlet

for i in range(len(input_lines)): 
    input_lines[i] = int(input_lines[i]) 
input_lines.sort()

input_lines.append(max(input_lines)+3) # add built in adapter

print(input_lines)
print(len(input_lines))

differences = []

for n, i in enumerate(input_lines):
    if n == len(input_lines)-1:
        break
    differences.append(input_lines[n+1]-i)
    
print(differences)

ones = differences.count(1)
threes = differences.count(3)

print("1 =",ones)
print("3 =",threes)
print("Answer=",int(ones*threes))