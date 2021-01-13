def employeeinfo(employ_name, employ_id, employ_address, employ_email):    
    #creating employee name loop
    employee_info ={'Employee name': employ_name, 'Employee id': employ_id,'Employee email': employ_email, 'Employee Address': employ_address}

    program_run = 0 
    #creating loop to fill in formation
    while program_run < 5:
        name_run = False
        while not name_run:
            bad_char = ["!", "#","@", "$", "%", "^", "&", "*", "(", ")" , "=", "+", ",", "<", ">","""""","'", "/", "?", ":",";", "[", "]","{","}", "\""]

            if employ_name:
                employ_name_prompt = ("Please enter Employee Name: ")
                for character in employ_name:
                    if character in bad_char:
                        print("Your Employee address is " + employ_name)
                    else:
                        address_run = False

            else:
                name_run = True 
    #creating employee id loop  
    #creating loop to fill in formation
    
        num_run = False
        while not num_run:
            if employ_id.isdigit():
                employ_id_prompt = ("Please enter Employee ID: ")
                if len(employ_id) <= 7:
                    num_run = True
                    print("Your Employee ID is "+ employ_id)
                else:
                    num_run = False
                    print("error found")
                    break

            else:
                num_run = True
                break
        
    #creating a bad character list
    #creating employee email loop
    #creating a bad character loop
    #creating loop to fill in formation   
        email_run = False
        while not email_run:
            bad_char = ["!", " #", "$", "%", "^", "&", "*", "(", ")" , "=", "+", ",", "<", ">","""""","'", "/", "?", ":",";", "[", "]","{","}", "\""]

            if employ_email:
                employ_email_prompt = ("Please enter Employee email ")
                for character in employ_email:
                    if character in bad_char:
                        print("Your Employee address is " + employ_email)
                    else:
                        address_run = False
            else:
                email_run = True
           
    #creating a bad character list
    #creating employee email loop
    #creating a bad character loop
    #creating employee Address loop
    
        address_run = False
        while not address_run:
            bad_char = ["!", "#","@", "$", "%", "^", "&", "*", "(", ")" , "=", "+", ",", "<", ">","""""","'", "/", "?", ":",";", "[", "]","{","}", "\""]
#creating loop to fill in formation
            if employ_address:

                employ_address_prompt = ("Please enter Employee Address ")
                for character in employ_email:
                    if character in bad_char:
                        print("Your Employee address is " + employ_address)
                    else:
                        address_run = False

            else:
                address_run = True 