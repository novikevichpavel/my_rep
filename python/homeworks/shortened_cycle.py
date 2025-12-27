# Задача 1
# Создать словарь, где значения ключей - строки
# Создать новый словарь, и с помощью сокращенного цикла внести значения из предыдущего, но значения ключей в верхнем регистре
# Вывести результат в терминал

my_dict = {
    "name": "pavel",
    "surname": "novikevich"
}
upper_case_dict = {key: value.upper() for key, value in my_dict.items()}
print(upper_case_dict)


# Задача 2
# Создать список, содержащий строки
# Создать новый список, с помощью сокращенного цикла знаести в него значения с длинной более 3 символов из предыдущего цикла
# Вывести результирующий список в терминал

orig_list = ["d", "df", "pavel", "dgt", "polina", "oksana", "volga"]
true_list = [elem for elem in orig_list if len(elem) > 3]
print(true_list)