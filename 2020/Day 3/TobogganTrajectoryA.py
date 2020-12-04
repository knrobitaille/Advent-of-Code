import pandas as pd
df = pd.read_csv('tree_grid.csv',names=['Map'])
# print(df.head())

tg_list = df['Map'].values.tolist()
# print(tg_list)


right = 3
length = len(tg_list[0])

right_index=0
trees = 0

for n, i in enumerate(tg_list):
    # print('checking line',n,i,'index',right_index)
    tile = i[right_index]
    if tile == '#':
        trees +=1
    right_index += right
    if right_index >= length:
        right_index -= length
        
print('trees seen:',trees)
    