# Задача
# 1. Создать функцию image_info с одним параметров типа dict
# 2. Функция ожидает словарь, в ктором должно быть минимум два ключа: image_id; image_title;
# 3. Функция должна возвращать строку такого вида: 'Image 'my_cat' has id 5136'
# 4. Если хотя бы одного из этих ключей в словаре нет, функция должна генерировать ошибку TypeError
# 5. Вызвать функцию и корректно обработать ошибку в случае возникноваения


def image_info(**my_dict):
    if ('name' not in my_dict) or ('id' not in my_dict):
        raise TypeError('The image must have name and id')
    return f'Image \'{my_dict['name']}\' has id {my_dict['id']}'

try:
    print(image_info(name='My cat', id=53412424))
except TypeError as e:
    print(e)











    