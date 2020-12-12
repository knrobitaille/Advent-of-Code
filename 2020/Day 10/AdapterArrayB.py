# I struggled with this problem and ending up leaning on the below for help
# https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfdfthy?utm_source=share&utm_medium=web2x&context=3

input_file = open('jolt_adapters.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines)


for i in range(len(input_lines)): 
    input_lines[i] = int(input_lines[i]) 
input_lines.sort()

last = max(input_lines)
# print("Last number in input",last)
index = [1,0,0] + [0] * last
# print("Index\n",index)


for r in input_lines:
    # print("\n\n\nr is",r)
    # print(input_lines)
    # print("\n")
    # print(index[r]," = ",index[r-1]," + ",index[r-2]," + ",index[r-3])
    index[r] = index[r-1] + index[r-2] + index[r-3]
    # print("\n",index)
    if r == last:
        print("Answer is",index[r])
        break

