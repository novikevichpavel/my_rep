# 1. Создать пустой словарь
# 2. Трижды попрсоить пользователя сначала ввести название ключа, а потом ввести значение для этого ключа. Всего должно быть 6 запросов ввода
# 3. Во время получения данных от пользователя добавлять в словарь ключи со значениями согласно тому, что ввел пользователь
# 4. Вывести результат в терминал

# 1  Варинат решения:

my_dict = {}

for i in range(3):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

print(my_dict)


# 2  Вариант решения (от преподователя):

new_dict = {}

key_one = input("Enter key one: ")
value_one = input("Enter value one: ")
new_dict[key_one] = value_one

key_two = input("Enter key two: ")
value_two = input("Enter value two: ")
new_dict[key_two] = value_two

key_three = input("Enter key three: ")
value_three = input("Enter value three: ")
new_dict[key_three] = value_three

print(new_dict)