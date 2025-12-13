# Задача 1
# 1. Переписать вызов функции merge_list_to_dict из файла homework_function так, чтобы в нем использовались аргументы с ключевыми словами
# 2. Добавить еще один вызов функции, в котором будет один позиционный аргумент, а второй аргумент с ключевым словом

list_one = ['name', 'age', 'is_adult']
list_two = ['Pavel', 26, True]

def merge_list_to_dict(list_one, list_two):
    general_list = zip(list_one, list_two)
    merged_list = dict(general_list)
    return merged_list

print(merge_list_to_dict(list_one=list_one, list_two=list_two))
print(merge_list_to_dict(list_one, list_two=list_two))







# Задача 2
# 1. Создать функцию update_car_info, в которой все именованые аргумены будут объединяться в словарь car
# 2. Добавить в словарь новый ключи is_available со значением True
# 3. Вызввать из функции измененный словарь
# 4. Вызвать функцию с именоваными аргументами brand / price, их значения могут быть любыми 
# 5. Выведите в терминал результат функции



def update_car_info(**car_info):
    car_info['is_available'] = True
    return car_info

print(update_car_info(brand='BMW', price=25000))
