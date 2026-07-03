#class - blueprint for objects. It is like a collection of attributes. 

#when you create an object with a class , the object inherits the attributes of the class

#Dog — class with name and breed attributes, a bark() method that prints "{name} says Woof!".


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof !!")


bruce = Dog("Bruce", "Husky")

bruce.bark()


