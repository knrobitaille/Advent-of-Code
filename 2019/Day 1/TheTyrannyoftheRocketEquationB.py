input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

def find_fuel(mass):
    answer = mass // 3 - 2
    if answer <= 0:
        return 0
    else:
        return answer + find_fuel(answer)

def find_total_fuel(mass_list):
    answer = 0
    for mass in mass_list:
        answer += find_fuel(int(mass))
    return answer

answer = find_total_fuel(input_lines)

print("Answer:",answer)