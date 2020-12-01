import pandas as pd
df = pd.read_csv('expense_report.csv',names=['Expenses'])
# print(df.head())

expense_list = df['Expenses'].values.tolist()
# print(expense_list)

TARGET = 2020
answer = 0

for n1 in expense_list:
    for n2 in expense_list:
        if (TARGET - n1 - n2) in expense_list:
            answer = (TARGET - n1 - n2) * n1 * n2
    
print("The answer is",answer)