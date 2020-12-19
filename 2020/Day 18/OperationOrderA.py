import copy

input_file = open('homework.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

def solve(elist):
    while len(elist) > 1:
        string = str(elist[0])+elist[1]+str(elist[2])
        string_eval = eval(string)
        del elist[0:3]
        elist.insert(0,string_eval)
    return str(elist[0])


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
                        exp.insert(na,solve(eval_list))
                        break
                break
        # print("Expresion is",exp)
                    
        if not p_found:
            break
            
    while len(exp) > 1:
        first_three = exp[0:3]
        exp = [solve(first_three)] + exp[3:]

    # print(exp)
    all_answers.append(int(exp[0]))
    
# print(all_answers)
print("Puzzle answer is",sum(all_answers))
            

