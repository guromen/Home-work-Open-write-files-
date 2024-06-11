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

# print(cook_book['Омлет'][0]['ingredient_name'])
# print(cook_book['Омлет'][1]['ingredient_name'])
# print(cook_book['Омлет'][2]['ingredient_name'])

def get_shop_list_by_dishes(dishes, person_count):
    total = {}
    for dish in dishes:
        if dish in cook_book:
         for exist in cook_book[dish]:
            if exist['ingredient_name'] not in total:
                total[exist['ingredient_name']] = {'measure': exist['measure'], 'quantity': int(exist['quantity'])*person_count}
            else:
                total[exist['ingredient_name']]['quantity'] += int(exist['quantity'])*person_count
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return total
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

