input_file = open('bus_sched.txt','r')
input_lines = input_file.read().splitlines()
input_file = input_lines
# print(input_lines)
# print(len(input_lines))

depart = int(input_lines[0])
buses = input_lines[1].split(",")

# print(depart,buses)

closest_bus = ""
closest_val = 1000

for bus in buses:
    if bus == 'x':
        continue
    # print("\n",depart,bus)
    time = depart % int(bus)
    dif = int(bus) - time
    # print(dif,closest_val)
    if dif < closest_val:
        closest_bus = bus
        closest_val = dif
        
print("You should wait for bus",closest_bus,"for",closest_val,"minutes")
print("Answer:",int(closest_bus)*closest_val)