class User():
    #crating a profile for user
    def __init__(self, first_name, last_name, age, username, likes, dislikes):
        #creating a describtions for the user
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.username = username.title()
        self.likes = likes
        self.dislikes = dislikes
    
    def describe_user(self):
        #creating a summary of the user
        
        print(self.first_name + " "+ self.last_name)
        print( " Age: " + self.age)
        print(self.username)
        print("Likes: " + self.likes)
        print("Dislikes: "+ self.dislikes)
        
    def greet_user(self):
        #welcoming the user back
        print("Welcome " + self.username + " We missed you...")