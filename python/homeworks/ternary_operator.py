# 1. Переписать пример используя if-else
# 2. Проверить длину строки используя тернарный опретор

# Пример:

my_img = ("1920", "1080")

info = f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else "Incorrect image format"

print(info)


if len(my_img) == 2:
    print("correct image format")
else:
    print("incorrect format")

print("String is long" if len(info) > 79 else "String is short")  