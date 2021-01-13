from classes.pet import Pet

class Cat(Pet):
    """a simple class for representing dogs"""
    def __init__(self, name, age):
        """initialize name and age variables/attributes for the Cat"""
        super().__init__(name, age)