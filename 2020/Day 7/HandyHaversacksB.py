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


def read_bag(bag):
    total_count = 0
    for held_bag in bag_dict[bag]:
        if held_bag != 'other bag':
            top_count = int(bag_dict[bag][held_bag])
            total_count += top_count
            
            bottom_count = top_count * read_bag(held_bag)
            total_count += bottom_count
    return total_count

print(read_bag('shiny gold bag'))