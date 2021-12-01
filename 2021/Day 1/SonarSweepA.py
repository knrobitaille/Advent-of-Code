input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
print(input_lines)
# print(len(input_lines))

prev = ''
count=0
for i in input_lines:
    if i > prev:
        count += 1
    prev = i
    
print(count)

# Above was quick and dirty, took 94 seconds