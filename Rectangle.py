class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

#Полиморфная функция
def print_area(shape):
#Не важно, какой тип у shape, главное, чтобы был метод area()
    print(f"Площадь фигуры: {shape.area()}")

#Пример Duck Typing
def process_sequence(sequence):
#Работает с любым объектом, поддерживающим len() и индексацию
    print(f"Длина: {len(sequence)}")
    print(f"Первый элемент: {sequence[0]}")


my_shape = Circle(10)
print(my_shape.area())
my_shape2 = Rectangle (10, 2)
print(my_shape2.area())

print_area(my_shape2)
print_area(my_shape)


#Пример имитации перегрузки методов

class Calculator:
    def add(self, *args):
        if all(isinstance(arg, (int, float)) for arg in args):
            return sum(args)
        if all(isinstance(arg, str) for arg in args):
            return ''.join(args)
        raise TypeError("Unsupported types for add operation")