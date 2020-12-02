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
    
    minimum = int(x[0].split('-')[0])
    maximum = int(x[0].split('-')[1])
    letter = x[1][0]
    pw = x[2]
    # print("The letter",letter,"must appear",minimum,"to",maximum,"times in", pw)
    
    letter_count = pw.count(letter)
    # print(letter,"found",letter_count,"times")
    if letter_count >= minimum and letter_count <= maximum:
        # print("Correct")
        correct_pw_count += 1
        
print("There are",correct_pw_count,"correct passwords")

