import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

input_file = open('nav_instructions.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines)
# print(len(input_lines))

north = 0
south = 0
east = 0
west = 0

waypoint_ns = 1
waypoint_ew = 10

sp_wp_x = []
sp_wp_y = []

for i in input_lines:
    sp_wp_x.append(waypoint_ew)
    sp_wp_y.append(waypoint_ns)
    
    command = i[:1]
    value = int(i[1:])

    
    if command == 'N':
        waypoint_ns += value
    if command == 'S':
        waypoint_ns -= value
    if command == 'E':
        waypoint_ew += value
    if command == 'W':
        waypoint_ew -= value
    
    if command == 'F':
        if waypoint_ns > 0:
            north += waypoint_ns * value
        else:
            south += abs(waypoint_ns) * value
        
        if waypoint_ew > 0:
            east += waypoint_ew * value
        else:
            west += abs(waypoint_ew) * value
            
    if command == 'L':
        if value == 180:
            waypoint_ns, waypoint_ew = -waypoint_ns, -waypoint_ew
        if value == 90:
            waypoint_ns, waypoint_ew = waypoint_ew, -waypoint_ns
        if value == 270:
            waypoint_ns, waypoint_ew = -waypoint_ew, waypoint_ns
    if command == 'R':
        if value == 180:
            waypoint_ns, waypoint_ew = -waypoint_ns, -waypoint_ew
        if value == 90:
            waypoint_ns, waypoint_ew = -waypoint_ew, waypoint_ns
        if value == 270:
            waypoint_ns, waypoint_ew = waypoint_ew, -waypoint_ns
    
    
# print("North",north)
# print("South",south)
# print("East",east)
# print("West",west)

n_s = north-south
e_w = east-west

print("The answer is",abs(n_s)+abs(e_w))


###########################################
### Bonus exercise: adding scatter plot ###
###########################################
# completely inspired by below post
# https://www.reddit.com/r/adventofcode/comments/kbusr8/2020_day_12_part_2_waypoint_scatterplot_over_time/
# Used top answer in below post to figure out color
# https://stackoverflow.com/questions/17682216/scatter-plot-and-color-mapping-in-python

t = []
for i in range(len(sp_wp_x)):
    t.append(i)

plt.scatter(sp_wp_x, sp_wp_y, s= 20, c = t)
plt.title("Waypoint Location")
plt.xlabel("West - East")
plt.ylabel("South - North")
plt.grid(True)
# plt.legend()
plt.show()