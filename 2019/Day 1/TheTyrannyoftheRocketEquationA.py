input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

def find_fuel(mass):
    return mass // 3 - 2

answer = 0
for mass in input_lines:
    answer += find_fuel(int(mass))

print("Answer:",answer)