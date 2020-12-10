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
        print("Satisfies requirements.")
    else:
        print("index",i,"number",n,"does not satisfy requirements.")
        break
    preamble.pop(0)
    preamble.append(n)
    # print(preamble)

    
