input_data = '256310-732736'
minimum,maximum = input_data.split('-')
minimum,maximum = int(minimum),int(maximum)

def check_for_digits(number,digits=6):
    number = str(number)
    if len(number) == digits:
        return True
    else:
        return False
def check_for_double(number):
    number = str(number)
    for n, i in enumerate(number):
        try:
            if i == number[n+1]:
                if n+2 <= len(number)-1:
                    if i == number[n+2]:
                        continue
                if n-1 >= 0:
                    if i == number[n-1]:
                        continue
                return True
        except:
            pass
    return False
def check_for_increasing(number):
    number = str(number)
    for n, i in enumerate(number):
        try:
            if int(i) <= int(number[n+1]):
                continue
            else:
                return False
        except:
            pass
    return True

valid = 0
for i in range(minimum,maximum+1):
    if check_for_digits(i) == False or check_for_double(i) == False or check_for_increasing(i) == False:
        continue
    valid += 1
print("Answer",valid)