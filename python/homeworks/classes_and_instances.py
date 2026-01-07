# 1. Создать класс Image
# 2. У каждого экземпляра класса Image должно быть три собственных атрибута: -resolution; -title; -extension;
# 3. В классе должет быть метод resize, с помощью которого можно менять разрешение изображения.
# 4. Создть несколько экземпляров класса Image и вызвать метож resize


class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension
        
    def update_resolution(self, new_resolution):
        self.resolution = new_resolution
        return self.resolution
        
        
    def __str__(self):
        return f"The image '{self.title}' has resolution like {self.resolution} and its extension is {self.extension}"
        

first_image = Image("1024x640", "My cat", "JPEG")
print(first_image)
first_image.update_resolution("1920x1080")
print(first_image)

second_image = Image("800x600", "My_dog", "PNG")
second_image.update_resolution("1680x940")
print(second_image)