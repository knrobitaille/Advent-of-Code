input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
print(input_lines)
# print(len(input_lines))


gamma = ''
epsilon = ''

checkdict = {}

for i in input_lines:
    for n, x in enumerate(i):
        # print(n, x)
        if n not in checkdict:
            checkdict[n] = [x]
        else:
            checkdict[n].append(x)
            
print(checkdict)

for k, v in checkdict.items():
    print(k,v)
    if v.count('1') > v.count('0'):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

        

  
print(gamma, epsilon)
print(int(gamma,2) * int(epsilon,2))
  

