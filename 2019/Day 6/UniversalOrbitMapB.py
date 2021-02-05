input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))
orbit_dict = {}
for i in input_lines:
    orbitted, orbits = i.split(')')
    orbit_dict[orbits] = orbitted

def get_path(planet,orbit_dict,path=[]):
    next_planet = orbit_dict[planet]
    if next_planet == 'COM':
        return path
    else:
        path.append(next_planet)
        return get_path(next_planet,orbit_dict,path)

you = get_path('YOU',orbit_dict,[])
san = get_path('SAN',orbit_dict,[])
for a in you:
    if a in san:
        i_you = you.index(a)
        i_san = san.index(a)
        break
print("Answer",i_you+i_san)