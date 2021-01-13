employ_name_prompt = int
employ_id_prompt =int
employ_email_prompt = int
employ_address_prompt = int
employ_info = int
employeeinfo = int



""" i managed to get one part of the function to py doc but i couldn't get the other one to pydocs"""
from functions.my_functionsassignment import employeeinfo
program_run = 0

program_ran = program_run + 1
Quit_prompt = ("Would you like to Add another Employee? Y or N? ")
while True:
    employ_name = input(employ_name_prompt)
    employ_id = input(employ_id_prompt)
    employ_email = input(employ_email_prompt)
    employ_address = input(employ_address_prompt)
    print("\n a list of new employees below:")
    employ_info = employeeinfo("hello my name is " + employ_name+ ", my id is " + employ_id + ", my email is " + employ_email + ", and my address is " + employ_address)
    print(employ_info)
    Quit = input(Quit_prompt)
    if Quit == 'Y':
        continue

    else:
        break
#printing out the polls