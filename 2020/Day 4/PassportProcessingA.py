input_file = open('batch_file.txt','r')
if_lines = input_file.readlines()
# print(if_lines)

total_count = 0
passports = {}
for i in if_lines:
    x = i.split()  
    if x == []:
        # print("End of passport\n")
        total_count += 1
    else:
        if not total_count in passports:
            # print("Reading new passport. Number",total_count)
            passports[total_count] = {}
        for part in x:
            # print("Key is",part.split(':')[0])
            # print("Value is",part.split(':')[1])
            passports[total_count][part.split(':')[0]] = part.split(':')[1]
# print("Passports:",passports)

VALID_PARAMETERS = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] # exclude 'cid'
valid_count = 0
for k, v in passports.items():
    valid = True
    for i in VALID_PARAMETERS:
        if i not in v:
            valid = False
    if valid == True:
        valid_count += 1
print("Out of",total_count,"passports,",valid_count,"are valid.")

