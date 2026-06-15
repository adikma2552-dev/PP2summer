class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

dog = Dog("Rex")
print(dog.name)


class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

car = Car("Toyota")
print(car.brand)