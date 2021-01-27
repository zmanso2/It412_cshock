#part 2
print("Enter 'Q' at any time to quit!")
#creating quit option
#creating dinner input options
while True:
    Monday = input("Pick Monday's dinner: ")
    #input for monday
    Tuesday = input("Pick Tuesday's dinner: ")
    #input for Tuesday
    Wednesday = input("Pick Wednesday's dinner: ")
    #input for Wednesday
    Thursday = input("Pick Thursday's dinner: ")
    #input for Thursday
    Friday = input("Pick Friday's dinner: ")
    #input for Friday
    Quit = input("Continue? Y or N ")
    #input for Quit
    if Quit =='n':
        break
        #end loop
    else:
        continue
        #start loop over again

with open("file\weekly_dinners.txt", "a") as dinner_out:
    dinner_out.write("Monday's dinner is " + Monday + '\n')
    #printing monday's dinner into txt file
    dinner_out.write("Tuesday's dinner is " + Tuesday + '\n')
    #printing Tuesday's dinner into txt file
    dinner_out.write("Wednesday's dinner is " + Wednesday + '\n')
    #printing Wednesday's dinner into txt file
    dinner_out.write("Thursday's dinner is " + Thursday + '\n')
    #printing Thursday's dinner into txt file
    dinner_out.write("Friday's dinner is " + Friday + '\n')
    #printing Friday's dinner into txt file

