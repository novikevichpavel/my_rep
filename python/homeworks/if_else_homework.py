# Задача 
# Создать функцию route_info, которой будет передаваться словарь
# Если в словаре есть ключ distance и его значение - целое число, вернуть строку "Disatance to your destination is <disatance>"
# Иначе если в словаре есть ключи speed и time вернуть строку "Distance to your distination is <speed * time"
# Иначе вернуть строку "no distance info is available"



dictionaries = [
    {
        "distance": 76,
        "city": "Minsk"
    },
    {
        "country": "Belarus",
        "city": "Brest"
    },
    {
        "speed": 55,
        "time": 2
    }
]

dict_one, dict_two, dict_three = dictionaries

def route_info(**info):
    if ("distance" in info) and (type(info['distance']), int):
        return f"Distance to your destinations is {info["distance"]}"
    
    if "speed" in info and "time" in info:
        return f"Distance to your destination is {info["speed"] * info["time"]}"
    
    return "no distance info is available"

print(route_info(**dict_one))
print(route_info(**dict_two))
print(route_info(**dict_three))
