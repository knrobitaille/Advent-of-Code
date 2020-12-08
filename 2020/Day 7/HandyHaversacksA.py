input_file = open('bag_rules.txt','r')
br_lines = input_file.read().splitlines()
# print(br_lines)


bag_dict = {}
for rule in br_lines:
    
    rule = rule.replace("bags","bag")
    
    bag_separate = rule.split(' contain')
    bag_dict[bag_separate[0]] = {}
    
    held_bags = bag_separate[1].split(",")

    for held_bag in held_bags:
        if held_bag[-1:] == '.':
            held_bag = held_bag[:-1]
        held_bag = held_bag.strip()
        bag_dict[bag_separate[0]][held_bag.split(" ", 1)[1]] = held_bag.split(" ", 1)[0]

# Recursive function to find bag. Looks simple but is difficult to think about and implement
def find_bag(bag,search_for):
    found = False
    for held_bag in bag_dict[bag]:
        if held_bag != "other bag":
            if (held_bag == search_for):
                found = True
            if (find_bag(held_bag,search_for)):
                found = True
    return found

answer = 0
for bag in bag_dict:
    if find_bag(bag,"shiny gold bag"):
        answer += 1
        
print ("The answer is",answer)
    