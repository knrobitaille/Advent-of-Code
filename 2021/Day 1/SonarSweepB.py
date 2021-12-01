input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
print(input_lines)
# print(len(input_lines))

A = []
B = []
C = []
sum_list=[]
loop_count=0
for i in input_lines:
    loop_count+=1
    print("\nLoop Count",loop_count)
    print(i)
    
    A.append(int(i))
    print("adding",i,"to A")
    if loop_count>1:
        B.append(int(i))
        print("adding",i,"to B")
    if loop_count>2:
        C.append(int(i))
        print("adding",i,"to C")
        
        
    if len(A)==3:
        sum_list.append(sum(A))
        A=[]
        print("A added to sum and blanked")
    if len(B)==3:
        sum_list.append(sum(B))
        B=[]
        print("B added to sum and blanked")
    if len(C)==3:
        sum_list.append(sum(C))
        C=[]
        print("C added to sum and blanked")
            
print(sum_list)

prev = sum(sum_list)
count=0
for i in sum_list:
    if i > prev:
        count += 1
    prev = i
    
print(count)    