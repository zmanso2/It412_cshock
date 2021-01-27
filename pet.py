class Pet():
    """a simple class for representing a pet"""
    def __init__(self, name, age):
        """initialize name and age variables/attributes"""
        self.name = name
        self.age = age
    
    def clean(self):
        """represents the act of cleaning the pet"""
        print(self.name + " is clean!")