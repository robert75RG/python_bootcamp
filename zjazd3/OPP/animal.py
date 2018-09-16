class Animal():
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def sound(self):
       return 'kncok kncok'

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

def test_creat_animal():
    animal = Animal("Strange something", 1000)
    assert animal.name == 'Strange something'
    assert animal.age == 1000

def test_creat_sound():
    animal = Animal("Strange something", 1000)
    animal.sound()

    assert animal.sound() == "kncok kncok"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)




def test_creat_cat():
    cat = Cat("Albert", 5)
    assert cat.name == 'Albert'
    assert cat.age == 5





def test_creat_dog():
    dog = Dog("Nina", 6)
    assert dog.name == 'Nina'
    assert dog.age == 6