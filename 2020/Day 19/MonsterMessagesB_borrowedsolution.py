# THIS NOT MY SOLUTION
# TAKEN FROM HERE
# https://topaz.github.io/paste/#XQAAAQAnCgAAAAAAAAA0m0pnuFI8c/fBNApcL1Y57OO7A++6puZ0JXJD/kBA29C/HOta3P9p+BHeTV45JG3dakoaAXufTQCuMSCrM908JfdUCKMTdVciHZCGEpf5Yk1dAAXBwmZE2X0cXQQJmUmI4FG+Ph+D+nIfhnkYdBHCPSAEc8elDbDk4dR8lkza37FF7vA+/sm+M77GjNUTTAB7enRY8imtootH1tuhW69nHowJZ2J7sv0euurJJaDZPbUvvPqiDb3RQuvuiJxN88MaPHiO+pvp6lMzsO0QDz5wWNi2cUDTLRiS/k8EZ80afTVkaH2E6vtroX05RQyjc7h1Yf3eFf4f8v2BWKCfH9iLgteU0yWih8xIUXfqOjYwS0AlQId5EH/xWTn01Wn/3HdWvUrVuUtI8e9RJI1NCVVCbS03ZAKiQzsi3YZxxCj7d8oN2hMqmIjYKBiycNyxSemSR8lCldMGidpd8KRPp3pfW07Jq5zKRfcqUV50tCU8NH1G4/fbcOY4UHQli40PwY031Vb8v0sp1CNxC4EAdX8Wyw07qFdIUJNkD3POItH6pPhsG3r3CTAart7LERoepfwsZeLyyzBlv7N+ZESGETJvGEZZAJSR0KgL+u22Ys11SsUQTkbC7hfE4t/E6xsGcHkBASNtV9C2gm+WZwibxX+5DPnVkIESAmhLw4QtAgPsGKaFe5l020QI4NLrx4G/HujXIoF9pOamxrAErfxWNJfOpp1+aZZ1yfjdRDT7NhQEBfE2iX+jyLcFzSGZ9L5lqe7tDnsAW2SHsIs9ZTcPzDxsB+vtOXcDQh+toIod7cURf1oEAAC0HRj/qbRyYd5/lzHGrO35IYbqLRKTtlgPDbQOPllY0Qbxw6bRNBTG9LFwk8nh0bMd4XzpBHcWN6D1k8q/6Vu24zT1A3sY6eJldPzvdfsXdujOLt2EvZ9XH+akwcZN6Yls+D1ZzCHF2Jt0mnoc59UvZ33J056fo+Fio9/uza77aU93MxvmAvDB+xyXuNoJDWLSHyQeBjRthIYZ6d9RL5+vzI1aq2wrdVp5C76vxoB79LSS2EFBV1KNxSfRFddXbtziYOFfujOq6SmrsEZi5pTRyG88Wrc/yfiiA7LLVWr3l3XV7tvejXNxQJ2731LjBRGGseQcY2s5iIFgF1fBJEzOSdvg9TjxJfjHwmskQmILnHK3ZLkqzc2ItdWgTD23FDYuy3eODWXcUK5x9Ul4l15x6v2YeF4lVm0N/8I0ueM=
#

import re

def import_data():
	groups = open("input.txt").read().split('\n\n')
	rules = create_rules(groups[0].split('\n'))
	messages = groups[1].split('\n')
	return rules, messages


def convert_to_int_if_possible(character):
	try:
		return int(character)
	except:
		return character

def create_rules(rules_data):
	rules = dict()
	for line in rules_data:
		rule_key, line = line.split(': ')
		character_groups = line.split(' | ')
		character_groups = [character_group.split(' ') for character_group in character_groups]
		character_groups = [[character.replace('"', '') for character in group] for group in character_groups]
		character_groups = [[convert_to_int_if_possible(character) for character in group] for group in character_groups]
		rules[int(rule_key)] = character_groups
	return rules

def rule_has_only_strings(rule):
	return all([isinstance(c, str) for group in rule for c in group])

def find_rule_with_only_strings(rules):
	for rule_key, rule in rules.items():
		if rule_has_only_strings(rule):
			return rule_key
	return None

def replace_reference_by_rule(rules, search_key, replacement):
	for key, rule in rules.items():
		for gidx, group in enumerate(rule):
			for cidx, c in enumerate(group):
				if c == search_key:
					rules[key][gidx][cidx] = replacement
	return rules

def convert_rules_to_regex(rules):
	while True:
		found_key = find_rule_with_only_strings(rules)
		if not found_key:
			break 

		found_rule = rules.pop(found_key)
		regex = convert_rule_to_regex(found_rule)	
		rules = replace_reference_by_rule(rules, found_key, regex)
	return rules

def convert_rule_to_regex(rule):
	return r'(' + '|'.join(['(' + ''.join([c for cs in group for c in cs]) + ')' for group in rule]) + ')'	

def count_valid_messages_by_regex(messages, regex):
	regex += r'$' # Include line-end in regex to match whole line
	p = re.compile(regex)
	count = 0
	for message in messages:
		match = p.match(message)
		if match: 
			count += 1
	return count

# Part 1
rules, messages = import_data()
rules = convert_rules_to_regex(rules)
regex = convert_rule_to_regex(rules[0])
print(rules,messages)
print(regex)
print('Answer 1:', count_valid_messages_by_regex(messages, regex))

# Part 2
rules, messages = import_data()

# Update rules
rules[8]  = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

rules = convert_rules_to_regex(rules)

regex42 = rules[8][0][0]
regex31 = rules[11][0][1]
regex8  = regex42 + '+'
regex11 = r'(' + '|'.join([f'{regex42}{{{n}}}{regex31}{{{n}}}' for n in range(1, 5)]) + ')'
regex0  = regex8 + regex11

print('Answer 2:', count_valid_messages_by_regex(messages, regex0))