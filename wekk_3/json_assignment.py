import json
import shutil
file_shot = ""
selectfile = ""

with open("json/basic_config.json") as json_ob:
    configdata = json.load(json_ob)
print(configdata)
#creating a loop to add files and values, and delete files

while True:
#creating a new file
    anewfile = input("Would you like to create a new File? Y or N ")
    if anewfile == "Y":
        selectfile = input("Enter in new File: ")
#creating a new value to a file
    anewvalue = input("Would you like to add a Value? Y or N ")
    if anewvalue == "Y":
        value = input("New value: ")
        configdata[selectfile] = value
    
    with open("json/config_override.json", "w") as json_ob:
        json.dump(configdata, json_ob)
    
    #deleting a file
    bdelfile = input("Would you like to delete a File? Y or N ")
    if bdelfile == "Y":
 
        selectfile = input("Enter in File name: ")
        if selectfile in configdata:
            configdata.pop(selectfile, None)

    #saving the file

 #seeing if they are finished to end the loop or to continue the loop   
    dcompletework = input("Would you like to continue? Y or N ")
    if dcompletework == "N":
        print("Thank You!")
        break
        