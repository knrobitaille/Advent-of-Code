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
            
    # This is certaintly not the best way to check parameters but it works
    if valid == True:
        for ka, va in v.items():
            
            if ka == 'byr':
                if not (int(va) >= 1920 and int(va) <= 2002):
                    valid = False
                    
            elif ka == 'iyr':
                if not (int(va) >= 2010 and int(va) <= 2020):
                    valid = False
            
            elif ka == 'eyr':
                if not (int(va) >= 2020 and int(va) <= 2030):
                    valid = False
            
            elif ka == 'hgt':
                if va[-2:] not in ['cm','in']:
                    valid = False
                else:
                    if va[-2:] == 'cm':
                        if not (int(va[:-2]) >= 150 and int(va[:-2]) <= 193):
                            valid = False
                    else:
                        if not (int(va[:-2]) >= 59 and int(va[:-2]) <= 76):
                            valid = False
                            
            elif ka == 'hcl':
                if not va[0] == '#' and len(va) != 7:
                    valid = False
            
            elif ka == 'ecl':
                if va not in ['amb','blu','brn','gry','grn','hzl','oth']:
                    valid = False
                    
            elif ka == 'pid':
                if len(va) != 9 or not(va.isdigit()):
                    valid = False
                    
            else:
                pass
        
        
    if valid == True:
        valid_count += 1
        
print("Out of",total_count,"passports,",valid_count,"are valid.")


"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
"""
        