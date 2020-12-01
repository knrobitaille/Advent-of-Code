import pandas as pd
df = pd.read_csv('expense_report.csv',names=['Expenses'])
# print(df.head())

expense_list = df['Expenses'].values.tolist()
# print(expense_list)

TARGET = 2020
answer = 0

for n in expense_list:
    if (TARGET - n) in expense_list:
        answer = n * (TARGET - n)
        break
    
print("The answer is",answer)