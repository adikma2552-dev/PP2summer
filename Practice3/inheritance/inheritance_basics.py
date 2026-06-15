class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass

dog = Dog()
dog.speak()


class Vehicle:
    def move(self):
        print("Moving")


class Car(Vehicle):
    pass

car = Car()
car.move()