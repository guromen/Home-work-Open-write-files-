cook_book = {}

with open('recipes.txt', encoding = 'utf-8') as f:   
    for line in f:
        name_dish = line.strip()
        count = int(f.readline())
        ingrigients = []
        for n in range(count):
            product = f.readline()
            ingredient_dict = {}
            item1, item2, item3 = product.strip().split(" |")
            ingredient_dict['ingredient_name'] = item1.strip(' ')
            ingredient_dict['quantity'] = int(item2.strip(' '))
            ingredient_dict['measure'] = item3.strip(' \n')
            ingrigients.append(ingredient_dict)
        cook_book[name_dish] = ingrigients        
        f.readline()
print(cook_book)
