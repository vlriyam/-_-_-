""" Иерархия "Транспортные средства"
 Создать базовый класс Vehicle (Транспортное средство) с атрибутами brand (марка) 
и model (модель). У него должен быть метод get_info(), который возвращает строку 
с маркой и моделью.
 Создать два класса-наследника:
 Car (Автомобиль), который добавляет атрибут num_doors (количество дверей) и 
переопределяет метод get_info(), добавляя в строку информацию о количестве 
дверей.
 Bicycle (Велосипед), который добавляет атрибут type (тип, например, "горный") и 
переопределяет метод get_info(), добавляя в строку тип велосипеда.
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def get_info(self):
        return f"{self.brand} {self.model}"
    
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        self.brand = brand
        self.model = model
        self.num_doors = num_doors
    def get_info(self):
        return f"Машина. \nБренд: {self.brand} \nМодель: {self.model} \nКоличество дверей: {self.num_doors}"

class Bicycle(Vehicle):
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
    def get_info(self):
        return f"Велосипед. \nБренд: {self.brand} \nМодель: {self.model} \nТип: {self.type}"
    

car = Car('BMW', 'e34', 4)
bicycle = Bicycle('BB', 's200', 'горный')

print(car.get_info())
print('--------------------------------------------')
print(bicycle.get_info())


