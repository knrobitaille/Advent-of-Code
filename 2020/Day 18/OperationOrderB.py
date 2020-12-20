import copy

input_file = open('homework.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

def solve_add_first(elist):
    # print("\nfunctionstart\nelist",elist)
    all_add = False
    while not all_add:
        # print("checking",elist)
        elistcopy = copy.deepcopy(elist)
        for i, n in enumerate(elistcopy):
            # print("check index",i,"char",n)
            if n == '+':
                # print("found +")
                sub = elistcopy[i-1]+elistcopy[i]+elistcopy[i+1]
                subsolved = str(eval(sub))
                # print(sub,"=",subsolved)
                del elist[i-1:i+2]
                elist.insert(i-1,subsolved)
                # print(elist)
                all_add = False
                break
            all_add = True
        
    exp = ''
    for i in elist:
        exp += i
        
    return str(eval(exp))


all_answers=[]
for line in input_lines:
    # print("\n",line)
    separated = line.split(" ")
    # print(separated)
    
    exp = []
    for e in separated:
        # print(e)
        if '(' not in e and ')' not in e:
            exp.append(e)
        else:
            for char in e:
                exp.append(char)
    # print(exp)
    
    expcopy = copy.deepcopy(exp)
    while True:
        expcopy = copy.deepcopy(exp)
        p_found = False
        for n in range(len(expcopy)):
            if ')' in exp[n]:
                p_found=True
                # print("Found ) at index",n)
                
                for na in range(n-1,-1,-1):
                    if '(' in exp[na]:
                        # print("Found ( at index",na)
                        # start_index = na
                        # end_index = n
                        eval_list = []
                        for i in range(na+1,n):
                            eval_list.append(exp[i])
                        # print(eval_list)
                        del exp[na:n+1]
                        exp.insert(na,solve_add_first(eval_list))
                        break
                break
        # print("Expresion is",exp)
                    
        if not p_found:
            break
            

        
    answer = solve_add_first(exp)
    print(answer)
    all_answers.append(int(answer))
print(all_answers)
print("Puzzle answer is",sum(all_answers))
 

