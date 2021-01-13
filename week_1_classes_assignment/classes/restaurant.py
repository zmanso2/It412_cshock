#9-1 problem 3
class Restaurant():
    #describtion of restauants
    def __init__(self, name, cuisine):
        #initializing name and cuisine of restaurants
        self.name = name.title()
        self.cuisine = cuisine.title()

    def Describe_restaurant(self):
        #describing the restaurant name and cuisine
        print(self.name + " serves " + self.cuisine)

    def restaurant_open(self):
        #telling people the restaurant is openned
        print(self.name + " is open today")