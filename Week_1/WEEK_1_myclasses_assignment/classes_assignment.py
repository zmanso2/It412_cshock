from classes.person import Person
from classes.instructor import instructor
from classes.student import student
from classes.vaildator import vaildator
"""importing all classes to be pulled over"""
""" tiny problem so unable to do py doc"""

while True:
    user_type_valid = false
    
    while not user_type_vaild:
        user_type = input("are you a student or instructor? (Enter I   or S)")
        user_type_valid = my_validator.isvalid(user_type)
        name_valid = false
    
    while not name_vaild:
        user_name = input("Please enter in name:  ")
        user_name= my_validator.isvalid(user_type)
        if user_type.lower() == "s":
            program_valid = false
           
            while not program_valid:
                program = input(" please enter your program")
                my_student = student(name, "email address", 1233, program)
                college_records.append(my_student)
                keep_going = input("do you want to continue ? (Y/N)")
                if keep_going.lower == "n":
                    break
for record in college_records:
    print(records.college_records)
