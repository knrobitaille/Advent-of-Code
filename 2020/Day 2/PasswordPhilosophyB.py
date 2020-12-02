import pandas as pd
df = pd.read_csv('password_list.csv',names=['Data'])
# print(df.head())

pw_list = df['Data'].values.tolist()
# print(pw_list)

correct_pw_count = 0

for i in pw_list:
    # print("\nChecking new password")
    x = i.split()
    # print("First index:",x[0])
    # print("Second index:",x[1])
    # print("Third index:",x[2])
    
    check1 = int(x[0].split('-')[0])
    check2 = int(x[0].split('-')[1])
    letter = x[1][0]
    pw = x[2]
    # print("The letter",letter,"must appear in only one of the following positions:",
    #       check1,"or",check2," in", pw)
    
    if letter in pw[check1-1] and letter not in pw[check2-1]:
        # print("Correct")
        correct_pw_count += 1
    elif letter not in pw[check1-1] and letter in pw[check2-1]:
        # print("Correct")
        correct_pw_count += 1
    else:
        pass

print("There are",correct_pw_count,"correct passwords")