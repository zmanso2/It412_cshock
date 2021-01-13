from classes.pet import Pet
class Dog(Pet):
    """a simple class for representing dogs"""
    def __init__(self, name, age, breed):
        """initialize name and age variables/attributes for the dog"""
        self.breed = breed

    def placeDoginCarrier(self):
        """This represents placing the dog in car carrier"""
        print(self.name + " is in the dog carrier!")

    def taketoVet(self):
        """contains all the task needed to get the dog to the vet"""
        self.placeDoginCarrier()
        self.__visitVet()

    def __visitVet(self):
        """represents the act of taking the dog to the vet"""
        print(self.name + " is on their way to the vet!")
