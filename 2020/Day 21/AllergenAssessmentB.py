input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))


class Food:
    def __init__(self,id_num,ingredients,allergens):
        self.id_num = id_num
        self.ingredients = ingredients
        self.allergens = allergens
        
all_foods = []
all_ingredients_list = []
ingredients_set = set()
allergens_set = set()

food = 0
ingredients = []
allergens = []
for line in input_lines:
    split = line.split("(contains")
    ingredients = split[0].strip().split()
    # print(ingredients)
    split[1] = split[1].replace(",","")
    allergens = split[1].strip(")").strip(",").split()
    # print(allergens)
    f = Food(food,ingredients,allergens)
    all_foods.append(f)
    
    all_ingredients_list.extend(ingredients)
    ingredients_set.update(ingredients)
    allergens_set.update(allergens)
    food+=1

# print(all_ingredients_list)    
# print("\nIngredients set:",ingredients_set,len(ingredients_set))
# print("\nAllergens set:",allergens_set,len(allergens_set))
# print()
    
match_dict = {}
for f in all_foods:
    # print("ID",f.id_num)
    # print("Ingredients",f.ingredients)
    # print("Allergens",f.allergens)
    # print()
    
    for a in f.allergens:
        if a not in match_dict:
            match_dict[a] = set(f.ingredients)
        else:
            to_remove = []
            for i in match_dict[a]:
                if i not in f.ingredients:
                    to_remove.append(i)
            for tr in to_remove:
                match_dict[a].remove(tr) 
                              
# print(match_dict)
  
          
final_dict = {}
finished = False
while not finished:
    finished = True
    for k,v in match_dict.items():
        # print(k,v)
        if len(v) == 1:
            final_dict[list(v)[0]] = k
        else:
            finished = False
            to_remove = []
            for i in v:
                if i in final_dict:
                    to_remove.append(i)
            for tr in to_remove:
                match_dict[k].remove(tr)
# print(final_dict)

dangerous_ingredient_list = sorted(final_dict, key=final_dict.get)
print("Answer is:\n"+",".join(dangerous_ingredient_list))

