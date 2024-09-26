import math

class Figure:
    sides_count = 0     #количество сторон

    def __init__(self, color, *sides):
        if len(sides) == self.sides_count:
            self.__sides = list(sides) #список сторон  (целые числа)
        else:
            self.__sides = [1]*self.sides_count
        self.__color = list(color)    #список цветов в формате RGB
        self.filled = True  #закрашенный, bool
        self.get_sides()

    def get_color(self):  # получить цвет
        return self.__color

    def set_color(self, r, g, b):   # собрать цвет
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):  #действительный цвет
        return 0 <= int(r) <= 255 and 0 <= int(g) <= 255 and 0 <= b <= 255
           # Цвет прежний

    def __len__(self):
        return sum(self.__sides)       #периметр фигуры
    def get_sides(self):     #получить стороны
        return self.__sides

    def set_sides(self, *sides):  # установить стороны
        if len(sides) == self.sides_count:
            self.__sides = list(sides)


    def __is_valid_sides(self, *sides): #значение стороны
        for i in self.__sides:
            if int(i) > 0:
                if len(sides) == self.sides_count:
                    return True

class Circle(Figure):    #Круг
    sides_count = 1   #количество сторон

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)


    def get_square(self):       #площадь
        return (self.__radius ** 2)*math.pi


class Triangle(Figure):     #треугольник
    sides_count = 3       #количество сторон

    def __init__(self, color, *sides):
        super().__init__(color, *sides)


    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2  # Полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))  # Площадь по формуле Герона


class Cube(Figure):  #Куб
    sides_count = 12  #количество сторон

    def __init__(self, color, sides):
        self._sides = [sides] * 12
        super().__init__(color, *self._sides)

    def get_volume(self):
        self.get_sides()
        return self._sides[0] ** 3

# Проверка на количество переданных сторон:
circle1 = Circle((200, 200, 100), 10, 6, 9)
print(circle1.sides_count)

triangle1 = Triangle((200, 200, 100), 10, 6, 13)
print(triangle1.sides_count)

cube1 = Cube((200, 200, 100), 9)
print(cube1.sides_count)

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
#
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
#
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

#Проверка объёма (куба):
print(cube1.get_volume())

#Площадь треугольника
print(triangle1.get_square())

#площадь круга
print(circle1.get_square())