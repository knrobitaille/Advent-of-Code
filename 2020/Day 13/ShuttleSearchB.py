from functools import reduce
import operator
# math.prod
# https://stackoverflow.com/questions/63727929/pycharm-module-math-has-no-attribute-prod

input_file = open('bus_sched.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines)
# print(len(input_lines))


buses = input_lines[1].split(",")
# print(buses)
# print(len(buses))


### Chinese Remainder Theorem
# I did not know about this and only found out from this puzzle
# I relied heavily on searching for solutions
# Found this persons solution and created a not as nice version:
# https://github.com/AidanGlickman/Advent-2020/blob/master/day13/solution.py
bus = []
ind = []
for i, t in enumerate(buses):
    if t != "x":
        bus.append(int(t))
        ind.append(int(t)-i)
# print(bus,ind)

sum_bus = 0
product = reduce(operator.mul, bus, 1)

for i, j in zip(bus,ind):
    p = product // i
    
    modinv = 0
    a = p
    b = i
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        modinv = 1
    else:
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        modinv = x1
    
    sum_bus += j * modinv * p
    
answer = sum_bus % product
print("Answer",answer)



### This would eventually work but literally take days
### This was the solution I came up with before finding out about the
### Chinese Remainder Theorem


# bus_dict = {}
# for n, bus in enumerate(buses):
#     if bus == 'x':
#         continue
#     bus_dict[int(bus)] = n

# step = 741745043105074
# run = True
# while run:
#     # print("Step",step)
#     found = True
#     for bus in bus_dict.keys():
#         if bus == 'x':
#             continue
#         if ((step + bus_dict[int(bus)]) % int(bus)) != 0:
#             found = False
#             continue  
#     if found:
#         print("Found! Step",step)
#         run = False
#     step += 1




