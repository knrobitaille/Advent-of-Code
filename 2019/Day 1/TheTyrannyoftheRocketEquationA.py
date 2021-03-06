input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

def find_fuel(mass):
    return mass // 3 - 2

def find_total_fuel(mass_list):
    answer = 0
    for mass in mass_list:
        answer += find_fuel(int(mass))
    return answer

answer = find_total_fuel(input_lines)

print("Answer:",answer)