class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        return "Some generic animal sound"
    def info(self):
        return f"{self.name} is a {self.species}"


class Dog(Animal): # Dog наследуется от Animal
    def __init__(self, name, breed):
        #Вызов конструктора родительского класса
        super().__init__(name, species="Dog")
        self.breed = breed
#Переопределение метода
    def make_sound(self):
        return "Woof!"
#Расширение функциональности
    def info(self):
        base_info = super().info()
        return f"{base_info} of breed {self.breed}"


#Множественное наследование
class ServiceDog(Dog, Animal):
    def __init__(self, name, breed, service_type):
        super().__init__(name, breed)
        self.service_type = service_type

    def perform_service(self):
        return f"{self.name} is helping as a {self.service_type}"

my_dog = Dog("Jon", "Doberman")

print(my_dog.info())
print(my_dog.make_sound())

