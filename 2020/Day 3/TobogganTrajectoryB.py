import pandas as pd
df = pd.read_csv('tree_grid.csv',names=['Map'])
# print(df.head())

tg_list = df['Map'].values.tolist()
# print(tg_list)

paths = [[1,1],[3,1],[5,1],[7,1],[1,2]]
length = len(tg_list[0])

trees = []

for path in paths:
    # print(path)
    right = path[0]
    down = path[1]
    cur_trees = 0
    right_index=0
    for n, i in enumerate(tg_list):
        if (n) % down == 0:
        # print('checking line',n,i,'index',right_index)
            tile = i[right_index]
            if tile == '#':
                cur_trees +=1     
            right_index += right
            if right_index >= length:
                right_index -= length
    trees.append(cur_trees)
        
# print('trees seen:',trees)

answer=1
for tree in trees:
    answer *= tree

print('final answer is',answer)

    