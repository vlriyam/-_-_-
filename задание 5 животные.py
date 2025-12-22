class Animal:
    def __init__(self, name, age, x=0, y=0):
        self.name = name
        self.age = age
        self.x = x
        self.y = y
    
    def run(self, new_x, new_y):
        self.x += new_x
        self.y += new_y
        return (self.x, self.y)
    
    def get_position(self):
        return (self.x, self.y)
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.name}: позиция ({self.x}, {self.y})"
    
    def info(self):
        pass

    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self, name, age,  x=0, y=0):
        super().__init__(name, age, x, y)

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

    def run(self, new_x, new_y):
        print(f"Новые координаты кошки: ({self.x + new_x}, {self.y + new_y})")
    
    def get_position(self):
        return (self.x, self.y)


class Dog(Animal):
    def __init__(self, name, age,  x=0, y=0):
        super().__init__(name, age, x, y)

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

    def run(self, new_x, new_y):
        print(f"Новые координаты собаки: ({self.x + new_x}, {self.y + new_y})")

class Bird(Animal):
    def __init__(self, name, age,  x=0, y=0):
        super().__init__(name, age, x, y)

    def info(self):
        print(f"I am a bird. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Chirik")
    
    def run(self, new_x, new_y):
        print("Новые координаты птицы: ({self.x + new_x}, {self.y + new_y})")


cat1 = Cat("Kitty", 2.5, 1, 1)
dog1 = Dog("Fluffy", 4, 3, 7)
bird1 = Bird("Roy", 1, 0, 0)

for animal in (cat1, dog1, bird1):
    animal.make_sound()
    animal.info()
    animal.run(1, 1)
