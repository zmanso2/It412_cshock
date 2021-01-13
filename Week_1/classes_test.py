class Pet():
    """a simple class reresentation pet"""

    def __init__(self, name, age):
        """setting name and age variables/attributes"""
        self.name = name
        self.age = age
    
    def clean(self):
        """Represents cleaning pet"""
        print(self.name + "is clean!!")

class Dog(Pet):
    """a simple class for representing a dog"""

    def __init__(self, name, age, breed):
        """setting name and age variables/attributes for dog"""
        super().__init__(name, age)
        self.breed = breed

    def DoginCarrier(self):
        