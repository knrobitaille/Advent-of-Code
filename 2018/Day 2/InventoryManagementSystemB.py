input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)


count = 0
for i in input_lines:
    # print(i)
    for k in input_lines[count+1:]:
        false_count = 0
        counter = len(i)
        for n in range(counter):
            # print(n)
            if i[n] != k[n]:
                false_count += 1
                if false_count == 2:
                    break
        if false_count == 1:
            print(i,k)
            break
            