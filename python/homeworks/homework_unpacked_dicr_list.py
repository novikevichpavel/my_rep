# Создать список словарей(пример из двух)
# Распаковать список в переменные, соответсвенно присвоив словари этим перенменных
# Создать функцю, которая будет принимать два аргумента
# Распаковать словари в функцию и вызывать ее трижды


list_dict = [
    {
        'name': 'Pavel',
        'age': 26
    }, 
    {
        # 'name': 'Polina',
        'age': 21
    },
    {
        'name': 'Oksana',
        'age': 32
    }
]

dict_one, dict_two, dict_three = list_dict

def get_info(name=None, age=None):
    if age is None or name is None:
        raise TypeError('Please, put here only two arguments dict')
    return f'User {name} is {age} years old'

try:
    # print(get_info(**dict_one))
    print(get_info(**dict_two))
    # print(get_info(**dict_three))
except TypeError as e:
    print(e)