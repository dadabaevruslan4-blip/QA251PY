from abc import ABC, abstractmethod

#Абстрактный базовый класс
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Вычисляет площадь фигуры"""
        pass
    @abstractmethod
    def perimeter(self):
        """Вычисляет периметр фигуры"""
        pass
    def describe(self):
        """Неабстрактный метод с реализацией по умолчанию"""
        return f"Это фигура с площадью {self.area()} и периметром {self.perimeter()}"

#Конкретная реализация
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

#Использование
#shape = Shape() # Ошибка: нельзя создать экземпляр абстрактного класса
rectangle = Rectangle(5, 10)
print(rectangle.area()) # 50
print(rectangle.perimeter()) # 30
print(rectangle.describe()) # "Это фигура с площадью 50 и периметром 30"