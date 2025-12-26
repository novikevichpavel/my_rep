# Задача 1

# 1. Создать функцию dict_to_list, которая будет конвертировать словарь в список кортежей
# 2. Функция должна принимать словарь, а вовращть список кортежй, в каждом кртеже должны быть пары ключ/значение из словаря
# 3. Если значение - целое число, то его нужно умножить на два перед добавление в кортеж

my_dict = {
    "name": "Pavel",
    "age": 26
}


def dict_to_list(dict_to_convert):
    new_list = []
    for k, v in dict_to_convert.items():
        if type(v) is int:
            v *= 2
        new_list.append((k, v))
        
    return new_list

print(dict_to_list(my_dict))




# Задача 2

# 1. Создать функицю filter_list, которая будет фильтровать список 
# 2. У функции должно быть два параметра - список и тип значения
# 3. Функция должна вернуть новый список, в котором остнутся только значения того типа, который был передан в вызове функции кторым аргументом

my_list = [1, 2.4, 14.1, 702.445, "abc", True, 14, 7]

def filer_list(list_to_filter, value_type):
    new_list = []
    for item in list_to_filter:
        if type(item) is value_type:
            new_list.append(item)
    return new_list

print(filer_list(my_list, int))





