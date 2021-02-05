input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))
def count_orbit(planet,orbit_dict):
    next_planet = orbit_dict[planet]
    if next_planet == 'COM':
        return 1
    else:
        return 1 + count_orbit(next_planet,orbit_dict)
orbit_dict = {}
for i in input_lines:
    orbitted, orbits = i.split(')')
    orbit_dict[orbits] = orbitted
planet_set = set(orbit_dict)
direct = 0
for planet in planet_set:
    if planet == 'COM':
        continue
    else:
        direct += count_orbit(planet, orbit_dict)
print("Answer",direct)