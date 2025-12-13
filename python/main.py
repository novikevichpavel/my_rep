# ---------------- Методы строк ------------------------

# my_name = input("Enter your name: ")

# text = str.maketrans("", "", "aeyuiojh")

# trnslt = my_name.translate(text)

# print(trnslt.lower())



# ---------------  String  -------------------

# long_str = "This is a very long string"
# print(long_str)
# print(type(long_str))
# print(id(long_str))


# doc_str = """That is  the most
# longer string in this file. I created that jusr for trainng in creating string"""

# other_doc_str = doc_str.replace("created", "OOOOOO")

# print(other_doc_str.count("z"))
# print(len(other_doc_str))
# print(other_doc_str)
# print(other_doc_str[0], other_doc_str[1])
# print(other_doc_str[:10])




#  ------------------- Integer -------------------------

# friends_qty = int(input("Input num: "))
# print(type(friends_qty))


# Возведение в степень

# base = 5
# power = 3
# print(type(pow(base, power))) 



# --------------- Float -------------------

# float_price = 27.55
# print(type(float_price))

# convert_float = int(float_price)
# print(type(convert_float))


# Округление

# price_one = 7.25
# print(round(price_one))

# price_two = 7.88
# print(round(price_two))


# Комлпексное число
# Состоит их действительной и мнимой части (j)

# complex_a = 10 + 7j
# complex_b = 3 + 3j

# complex_sum = complex_a * complex_b
# # (10 + 7j)*(3 + 3j) = 30 + 30j + 21j - 21

# print(complex_sum)

# print(type(complex_sum))




# ------------------- Boolean ----------------------

# --------------------- Конвертация ------------------

# int_num = 5
# float_num = 4.5
# print(int_num + float_num)
# print(float_num.__radd__(int_num))
# print(int_num.__add__(float_num))
# print(float_num.__rmul__(int_num)) # 4.5 * 5



# --------------- Списки в пайтон ---------------

# my_fruits = ["banana", "lime", "apple"]
# other_fruits = ["banana", "lime", "apple", "coconut"]
# my_fruits[1] = "ololosh"
# del other_fruits[3]
# print(my_fruits == other_fruits)
# print(my_fruits[1])
# print(len(other_fruits))


# users = [
#     {
#         "name": "Pavel",
#         "email": "novkevichp@gmail.com",
#     },
#     {
#         "name": "Polina",
#         "email": "kazakevicp59@gmail.com"
#     }
# ]

# print(len(users))
# print(users[0]["email"]) 



# yellow_fruit = "banana"
# green_friut = "apple"
# is_not_fruit = "cucumber"

# all_items = [yellow_fruit, green_friut, is_not_fruit]

# all_items.append("sayonara")
# print(all_items)

# all_items.pop(0)
# print(all_items)


# posts = [2, 15, 75, 3, 101]

# posts.sort() # Аргумента применится сортировка по умолчанию(по возрастанию)
# print(posts)

# posts.sort(reverse=True) # Сортировка по убыванию
# print(posts)


# message = "Hello from Python"
# list_message = list(message)
# print(list_message) # Будет создна список, где элементами будут каждая буква

# my_dict = {"a": 10, "b": True}
# dict_to_list = list(my_dict)
# print(dict_to_list) # В список попадут только ключи

# new_list = [2.5, 3.1, 4, 4.5]
# print(min(new_list)) # Минимальное значение из списка
# print(max(new_list)) # Максимальное значние из списка
# print(sum(new_list)) # Сумма элементов списка
# print(sum(new_list)/len(new_list)) # Сумма элементов списка делится на кол-во(длину) списка


# first_list = [1, 2, 4]
# second_list = [3, 5, 6]
# general_list = first_list + second_list # Обединение списков в один
# print(general_list)
# general_list.sort()
# print(general_list)


# my_list = [1, 2, 3, 4, 5, 6, 7]
# first_two_elem = my_list[:2] # Два первых элемента списка
# print(first_two_elem)
# without_first_last = my_list[1:-1] # Все кроме первого и последнего элементов списка
# print(without_first_last)
# last_two_elem = my_list[-2:] # два последних элемента списка
# print(last_two_elem)


# Копирование списков
# 1 Вариант
# cars = ["Audi", "BMW"]
# my_cars = cars[:]
# my_cars.append("Mercedes") # Добавит новый элемент в скопировный список не изменяя список из которого копировался этот
# print(cars)
# print(my_cars)
# print(id(cars) == id(my_cars)) # Покажет, что созданы два элемента, а не один

# 2 Вариант. Более предпочтительный за счет того, что явно видно копирование
# cars = ["Audi", "BMW"]
# my_cars = cars.copy()
# my_cars.append("Mercedes")
# print(my_cars)
# print(cars)
# print(id(my_cars) == id(cars))

# 3 Вариант
# cars = ["Audi", "BMW"]
# my_cars = list(cars)
# my_cars.append("Mercedes")
# print(my_cars)
# print(cars)
# print(id(my_cars) == id(cars))


# my_list = [1, 2, 3, 3, 4, 5, 6, 7]
# print(my_list.count(3)) # Кол-во раз, сколько встр в этом списке элемент 3
# my_list.insert(2, -5) # Добавит элемент 5, перед элементов со вторым индексом
# print(my_list)
# my_list.extend("abc") # Будте добвлен каждый результирующий элемент. То есть будет жобавлено три новых элемента
# print(my_list)






# ------------------- Словари ---------------

# my_motor_bike = {
#     "barnd": "Ducati",
#     "price": 25000,
#     "engine_vol": 1.2
# }

# print(my_motor_bike["price"]) # Вернет значение ключа price

# my_motor_bike["price"] = 17000 # Изменит значение ключа
# print(my_motor_bike)

# my_motor_bike["is_new"] = True # Добавит новый клбч со значением
# print(my_motor_bike)

# del my_motor_bike["engine_vol"] # Удалит ключ со значением из словаря
# print(my_motor_bike)


# Использование переменных в словарях

# my_motor_bike = {
#     #"brand": "Ducati",
#     "price": 25000,
#     "engine_vol": 1.2
# }

# print(my_motor_bike)

# key_name = "brand"
# my_motor_bike[key_name] = "BMW" # Добавит к словарю ключ с названием переменной, и добавит значение которок присвоено
# print(my_motor_bike)


# Вложенные словари 

# my_motor_bike = {
#     "brand": "Ducati",
#     "price_info": {
#         "price": 25000,
#         "is_available": True
#     },
#     "engine_vol": 1.2
# }

# print(my_motor_bike["price_info"]["is_available"]) # Доступ к значение ключа вложенного словаря


# Создание значений ключей с помощью переменных

# brand = "BMW"
# bike_price = 25000
# engine_vol = 1.2

# my_motorbike = {
#     "brand": brand,
#     "price": bike_price,
#     "engine_vol": engine_vol
# }

# print(my_motorbike)
# print(len(my_motorbike)) # Вернут длину словаря
# del my_motorbike["price"] # Удалить элемент со значением pirce
# print(len(my_motorbike)) # Вернет новую длину словаря


# Несуществубщию ключи и метод get

# my_motorbike = {
#     "brand": "BMW",
#     "price": 25000,
#     "is_available": True,
#     "engine_vol": 1.2
# }

# print(my_motorbike.get("manufacturer")) # Вернет None. если использовать стандартный синтаксис my_motorbike["manufacturer"] без обработки ошибки - будет вызвана внутренняя ошибка и выполнение кода будет остановлено

# print(my_motorbike.get("manufacturer", 0)) # Вместо None будет возвращен 0. Опционально для выполнения. Носит косметический характер на случай отсутствия ключа словаре

# print(my_motorbike.get("brand", 0)) # В данном случае вернут значения из словаря, так как такой ключ есть


# Практика

# my_disk = {}

# print(id(my_disk))
# print(type(my_disk))

# my_disk["brand"] = 'Samsung'
# my_disk["price"] = 80
# my_disk["country_of_manufcturer"] = "Korea"

# print(my_disk)
# print(id(my_disk))

# print(my_disk.items()) # Вернет специальный объект класса dict_items в виде списка с кортежами

# print(my_disk.keys()) # Вернет ключи словаря

# print(my_disk.popitem()) # Удаляет последний добавленный ключ со значением. Здесь, благодаря методу print будут выведен последний ключ, который был удален. Не рекуомендуется использовать

# print(my_disk)

# Копирование словарей

# my_disk = {}

# my_disk["brand"] = "Samsung"
# my_disk["price"] = 80

# new_disk = my_disk.copy() # Создасть новый словарь на основе старого не изменяя его

# new_disk["country"] = "Korea"
# print(new_disk)
# print(my_disk)
# print(len(new_disk)) # 3


# Конвертация других значений в словарь

# my_list = [["1", 2], ["b", True], ["c", "abc"]]

# my_dict = dict(my_list) # Бедет создан словарь на основе списка с вложенными списками. так же можно создавать словарь на основе списков кортежей. ВАЖНО, чтобы список списков или список кортежей имели по два элемента, то есть вложенные списки или вложенные кортежи имели два элемента, для того чтобы пайтон мог правильно конвертировать их в словарь

# print(my_dict)




# -------------------------- Кортежи --------------------

# Как и для списков, и для словарей можно использовать метод len() для получени] длины кортежа

# Можно получать определенные элементы кортежа, как и в списках print(my_tuple[0])

# Изменять значение элементов кортежа нельзя. print(my_tuple[0]) = 550. Будет вызвана ошибка

# Удалять элементы из кортежа нельзя. del my_tuple[1]. Будет вызвана ошибка

# Кортеж может содержать вложенные изменяемые элементы. Например. словари. Вложенные изменяемые элементы можно изменять внутри кортежа

# my_tuple = (
#     {
#         "user_id": 1,
#         "user_name": "Pavel"
#     },
#     {
#         "user_id": 2,
#         "user_name": "Polina"
#     }
# )
# print(my_tuple[1]["user_name"])
# my_tuple[0]["user_id"] = 225
# print(my_tuple[0]["user_id"])


# Как и в словарях, как и в списках в кортеах можно использовать переменные

# var_one = "banana"
# var_two = "lime"

# my_tuple = (var_one, var_two)

# print(my_tuple)


# Функция get() в кортежах не доступна

# Кортежи можно объеденять с помощью оператора +

# Кортежи мимеют только два метода count() и index()

# Кортеж можно конвертировать в список




# ------------------------- Наборы ----------------------------

# Набор - это неупорядоченная последовательность элементов
# Набор содержит только уникальные элемента
# Изменять наборы можно (удаление, добавление)
# В наборах обычно сохраняют однотипные данные

# set_one = {"apple", "banana", "lime"}
# set_two = {151, 122, 123, 234}
# set_three = {True, "hi", 10.5}

# print(type(set_one))

# my_set = {151, 253, 151, 11, 722, 11}
# print(my_set) # Выведет только уникальные элементы. Дубликаты будут автоматически удалены во время вывода

# my_fruits = {"lime", "banana", "apple"}
# other_fruits = {"lime", "banana", "apple"}
# print(my_fruits == other_fruits) # Отобразит True. Так как наборы состоят из одинаковых элементов, а порядок в наборах не важен


# Обраться к элементам набора по индексу нельзя, так как в наборах нет индексов

# В набор нельзя добавлять изменяемые элементы list_set = {[1, 2]. [3, 4]}



# ---------------- Методы наборов -----------------------

# set_one = {"800x620", "1920x1080"}
# # print(set_one)
# set_two = {"1024x768", "800x620"}
# # print(set_one.union(set_two))
# # print(set_one|set_two)
# common_set = set_one.intersection(set_two)
# print(common_set)


# nums = {1, 2, 3}
# other_nums = {0, 1, 15, 13, 2, 3}
# print(nums.issubset(other_nums))
# print(other_nums.issuperset(nums))

# set_1 = {"a", "t", "s", "l"}
# set_2 = {"j", "g", "s", "t", "l"}

# print(set_1.difference(set_2))
# print(set_2.difference(set_1))
# set_2.remove("j")
# set_3 = set_2.copy()
# print(set_2)
# print(set_3)
# print(set_1.symmetric_difference(set_2)) # (a | b) - (a & b)




# -------------------- Диапозоны ------------------------

# Упорядоченная неизменяемая последовательность элементов

# my_range = range(7)
# print(type(my_range))
# print(my_range)
# print(list(my_range))

# new_range = range(10, 20, 3) # 10 - sart value; 20 - end value; 3 - step iterartion;
# print(list(new_range))
# print(new_range[3])


# Опциональное задание по диапозонам:
# Создать диапозон. Выполнить по нему итерацию, а значения записат ьв список

# new_list = []
# for n in range(0,20, 5):
#     new_list.append(n)
#     # print(new_list)

# print(new_list)



# Резюме по типам последовательностей. Сравнение типов последовательностей
# Список - изменяемый; важен порядок; может содержать одинаковые элементы;
# Кортежи - неизменяемый; важен порядок; может содержать одинаковые элементы; 
# Наборы - изменяемый; порядок не важен; не может содержать одинаковые элементы;
# Дипозон - неизменяемый; порядок важен; не может содержать одинаковые элементы; 
# Словарь - Изменяемый; не важен порядок; не может содержать одинаковые элементы; 
# Строка - неизменяемая; порядок важен; можт содержать одинаковые элементы; 










# -------------------------- Функция ZIP ----------------------------
# Позволяет формировать объекты на основне другз последовтельностей

# names = ['Pavel', 'Polina', 'Oksana']
# surnames = ['Novikevich', 'Kazakevich', 'Plaska']
# is_adult = [True, False, True]

# user_names = zip(names, surnames, is_adult)

# print(user_names)
# print(list(user_names)) # Список кортежей

# key_names = ['his_age', 'her_age', 'its_age']
# ids = [66, 764, 244534]

# dict_new = zip(key_names, ids)

# print(dict(dict_new))





# Опциональное задание. Создать два списка, с названием товаров и ценой. Конвертировать сначала в словарь, потмо в спиоск и вывести все в терминал

# item_names = ['кресло', 'диван', 'ковер']
# item_price = [460, 1340, 185]
# zipped_items  = zip(item_names, item_price)
# print(list(zipped_items))
# print(dict(zipped_items))






# -------------------------- Избежание изменений копий ------------------

# В этом варианте начальный словарь изменен не будет
# main_info = {
#     'name': 'Polina',
#     'is_instructor': False
# }

# copied_info = main_info.copy()
# copied_info['reviews_qty'] = 5
# print(main_info)
# print(copied_info)


# # Если словарь содержит вложенные элементы - ссылки на них сохраняются. А это значит, что при изменении вложенного элемента - также изменен будет первоначальный словарь. То есть метод copy() дает копию первого уровня.

# info = {
#     'name': 'Pavel',
#     'is_instructor': False,
#     'reviews': []
# }

# info_copy = info.copy()
# info_copy['reviews'].append('great course')

# print(info)
# print(info_copy)




# Для возможности копирования вложенных элемнтов необходимо использовать бибилиотеку deepcopy

# from copy import deepcopy

# general_info = {
#     'name': 'Pavel',
#     'is_instructor': False,
#     'reviews': []
# }

# copy_info = deepcopy(general_info)

# copy_info['reviews'].append('Wow. That`s great')

# print(general_info)
# print(copy_info)


 









# ------------------------------ Функции -----------------------------

# a = int(input('Num one: '))
# b = int(input('Num two: '))

# def calc_nums(a, b): # Аргументы
#     c = a + b
#     return f'Your result is {c}'

# print(calc_nums(a, b))



# Передача изменяемых объектов в функцию
# В этом примере изменится внешний объект словаря

def increase_person_age(person):
    person['person_age'] += 1
    return person

person_one = {
    'name': 'Pavel',
    'person_age': 26
}

increase_person_age(person_one)
print(person_one)


# Вариант без изменениявнешного объекта

def increase_age(person):
    person_copy = person_one.copy()
    person_copy['person_age'] += 1
    return person_copy

new_person = increase_age(person_one)
print(new_person)
print(person_one)






# Объединения аргументов в кортеж(tuple). Аргументов можнет передаваться, в таком случае, большое количество

def sum_nums(*args):
    return sum(args)

print(sum_nums(1, 2, 4))


# Позиционнеы аргументы. В них порядок важен

# def get_posts_info(name, posts_qty):
#     info = f'{name} wrote {posts_qty} posts'
#     return info

# print(get_posts_info('Pavel', 25))



# Аргументы с ключевыми словами(именованные). В них порядок не важен. Используюся для лучшей читабельности

def get_posts_info(name, posts_qty):
    info = f'{name} wrote {posts_qty} posts'
    return info

print(get_posts_info(name='Pavel', posts_qty=25))
print(get_posts_info(posts_qty=25, name='Pavel'))


# Объединение аргументов в словарь

def get_info_about_posts(**person):
    info = (
        f'{person['name']} wrote '
        f'{person['posts_qty']} posts'
    )
    return info

print(get_info_about_posts(name='Pavel', posts_qty=25))
