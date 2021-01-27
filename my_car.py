import json
#importing json to py
from functions import *
#importing function to py
print("Enter 'Q' at any time to quit")
#giving user an option to quit
while True:
    car_type = input("Car Type: ")
    #inputing type of car
    if car_type == 'Q':
        break
    #quit option
    car_year = int(input("Car Year: "))
    #inputing what year car was made
    if car_year == 'Q':
        break
    #quit option
    Quit = input("Change Car? Y or N ")
    #input to add another car or quit
    if Quit == 'n':
        break
    #end loop
    else:
        continue
    #restart loop


with open("files/my_cars.json") as json_obj:
    config_data = json.load(json_obj)
    #loading info into json
config_data["Car"] = car_type
config_data["Year"] = car_year
with open("files/my_cars.json", "w") as json_obj:
    json.dump(config_data, json_obj)
    #dumping info into json
config_data["Car"] = car_type
config_data["Year"] = car_year
