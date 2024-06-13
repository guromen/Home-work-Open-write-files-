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
            #Проверка на уже существующий ингридеент 
            if exist['ingredient_name'] not in total:
                total[exist['ingredient_name']] = {'measure': exist['measure'], 'quantity': exist['quantity']*person_count}
            else:
                #Пересчет количества
                total[exist['ingredient_name']]['quantity'] += exist['quantity']*person_count
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return total

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

# прочитать все три файла .txt, которые даны в исходных данных,
# В каждом файле пересчитать количество строк,
# Создать словарь, где ключам будет количество строк, а значением само содерждание файла с добавленными впереди 2 строчками (названием файла и количеством строк)
# Отсортировать словарь по ключам
# Записать в новый результирующий файл последовательно данные всех значений отсортированного словаря


def write_file(path1, path2, path3):
    path1 = '1.txt'
    path2 = '2.txt'
    path3 = '3.txt'

    my_dict = {}
    
    with open(path1, encoding='utf-8') as f1:
        file1 = f1.readlines()
        my_dict[(len(file1))] = (path1) + '\n' + (str(len(file1))) + '\n' + (''.join(file1)) + '\n'
    with open(path2, encoding='utf-8') as f2:
        file2 = f2.readlines()
        my_dict[(len(file2))] = (path2) + '\n' + (str(len(file2))) + '\n' + (''.join(file2)) + '\n'
    with open(path3, encoding='utf-8') as f3:
        file3 = f3.readlines()
        my_dict[(len(file3))] = (path3) + '\n' + (str(len(file3))) + '\n' + (''.join(file3))
    my_dict = dict(sorted(my_dict.items(), key=lambda item: item[0]))
    # print(my_dict)

    with open('write_file.txt', 'w', encoding='utf-8') as f:
        for _, v in my_dict.items():
            f.write(str(v))
    return

write_file('1.txt', '2.txt', '3.txt')