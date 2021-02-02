#Example
# card_key = 5764801 #8
# door_key = 17807724 #11

card_key = 9232416
door_key = 14144084

value = 1
subject_number = 7
modulo=20201227

value = 1
for i in range(1,modulo):
    value = (value*subject_number) % modulo
    if value == card_key:
        card_loops = i
        break

encryption = 1
for i in range(0,card_loops):
    encryption = (encryption*door_key) % modulo
print("Answer is:",encryption)

