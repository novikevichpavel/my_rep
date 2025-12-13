# 1. Создать вуйнкцию merge_list_to_dict
# 2. Функция должна иметь два параметра
# 3. Она должна объединять два списка, используя встр. функцию. zip
# 4. Конвертировать объект zip в словарь и вернуть его из функции
# 5. Вызвать функцию, передав ей два списка в качестве аргументов
# 6. Вывести результат функции в терминал


list_one = ['name', 'age', 'is_adult']
list_two = ['Pavel', 26, True]

def merge_list_to_dict(list_one, list_two):
    general_list = zip(list_one, list_two)
    merged_list = dict(general_list)
    return merged_list

print(merge_list_to_dict(list_one, list_two))




