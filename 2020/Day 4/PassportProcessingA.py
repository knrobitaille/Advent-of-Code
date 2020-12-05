import pandas as pd
df = pd.read_csv('batch_file.csv',names=['Passports'])
print(df.head())

pp_list = df['Passports'].values.tolist()
# print(pp_list)