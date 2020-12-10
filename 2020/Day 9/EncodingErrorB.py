input_file = open('port_numbers.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)

preamble_len = 25
preamble = input_lines[:preamble_len]
for i, n in enumerate(input_lines):
    if i < preamble_len:
        continue    
    requirements = False
    for ia, na in enumerate(preamble):
        look_for = int(n) - int(na)
        if str(look_for) in preamble:
            requirements = True
            break
    if requirements == True:
        pass
        # print("Satisfies requirements.")
    else:
        invalid_num = n
        # print("index",i,"number",n,"does not satisfy requirements.")
        break
    preamble.pop(0)
    preamble.append(n)
    # print(preamble)

print("The invalid numbers is",invalid_num)

for i, n in enumerate(input_lines):
    if n == invalid_num:
        continue
    total = 0
    index = i
    contig_range = []
    while total < int(invalid_num):
        total+= int(input_lines[index])
        contig_range.append(int(input_lines[index]))
        index += 1
        if total == int(invalid_num):
            print("range starts at",i,"and goes to",index)
            # print(contig_range)
            print("max",max(contig_range))
            print("min",min(contig_range))
            print("Answer:",max(contig_range)+min(contig_range))
            break

        
    
