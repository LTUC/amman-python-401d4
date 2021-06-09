from abc import abstractmethod

class Pet:
    count = 0 # class variable (global)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.count += 1 # Increment the count everytime we create a Pet (Cat or Dog)
        print(f'{self.name} object has been created')
    
    def greet(self):
        print(f"Hello this is {self.name} and I'm {self.age} months old")
    
    @abstractmethod # Abstraction
    def speak(self):
        pass

    @classmethod # Class Method
    def get_pets_count(cls):
        return cls.count
    
    



class Cat(Pet):
    # Instance method
    def speak(self): 
        print("Meooooooow!!!")

    def __str__(self):
        return f'This is a Cat: {self.name}'
    
    def __repr__(self):
        return f'Cat instance: {self.name}'



class Dog(Pet):
    def __init__(self, name, age, species):
        self.species = species
        super().__init__(name,age)
        
    def speak(self):
        print("Whooooof")

    @staticmethod # Static Method
    def get_characteristics():
        print('Dogs like to jump')

    def __str__(self):
        return f'This is a Dog: {self.name}'
    
    def __repr__(self):
        return f'Dog instance: {self.name}'



class Things:
    def __init__(self, name):
        self.name = name
        self.animals = []






if __name__ == '__main__':
    oscar = Dog('Oscar', 13, 'German Shipher')
    sherry = Cat('Sherry', 10)
    oscar.greet()
    sherry.greet()
    sherry.speak()
    oscar.speak()
    oscar.get_characteristics()
    # OR
    Dog.get_characteristics()

    print(Pet.get_pets_count())

    # print(dir(oscar))
    # print(Pet.x)
    # print(Pet.greet())        XX No can't do this XX
    # print(dir(Cat))
    # print('========')
    # print(dir(Pet))
    thing = Things('Some Stuff')
    thing.animals.append(1)
    thing.animals.append(oscar)
    thing.animals.append(sherry)
    print(oscar)
    print(sherry)




