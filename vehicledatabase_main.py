from classes.vehicledatabase_access import DB_Connect


my_db = DB_Connect('root','','vehicle_info')

vehicle_info = False
Vehicle_make = ""
Vehicle_Model = ""
VIN = ""
pervious_owner = ""
purchase_price = float()
sale_price = float()
Vehicle_description = ""
my_result = my_db.executeSelectQuery("SELECT * FROM vehicle_info")
print("Please Select Following Options by Number!")

while not vehicle_info:
    print("1. Show all vehicles \n" 
    "2. Add a vehicle \n"
    "3. Edit a vehicle\n"
    "4. Remove a vehicle\n"
    "5. Exit program")
    user_choice = input("which would you like to do? (1/2/3/4/5): ")
    if user_choice == "1":
        print(my_result)
    elif user_choice =="2":
        passed_make = input("Vehicle make: ")
        Vehicle_make = passed_make.isalpha()
        bad_char = [' !', '"', '@' ,'#',' $', '%', '^', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', '] ','{', '} ','~ ','|','.']
        Vehicle_Model = input("Vehicle Model: ")
        for char in bad_char:
            if char not in Vehicle_Model:
                bad_char_found = True
            else:
                print("Bad char found")
                break
        passed_vin = input("VIN: ")
        VIN = passed_vin.isalnum()
        good_char = [',','.','-',"'"]
        pervious_owner = input("Previous Owner: ")
        for char in good_char:
            if char in Vehicle_Model:
                bad_char_found = True
            elif bad_char_found == False:
                return pervious_owner
            else:
                print("Bad char found")
                break

        purchase_price = input("Purchased price: ")
        sale_price = input("Sales Price: ")
        Vehicle_description = input("Describe Vehicle: ")
        my_db.executeQuery('INSERT INTO  vehicle_info (Vehicle_make, Vehicle_Model, VIN, pervious_owner, purchase_price, sale_price, Vehicle_description)VALUES("'+Vehicle_make+ Vehicle_Model+ VIN+ pervious_owner+purchase_price+ sale_price+ Vehicle_description+'")')
        my_result.conn.commit()
        print(my_result)
    

    elif user_choice =="3":
        edit_info = input("what would you like to edit?\n Vehicle_make\n Vehicle_Model\n VIN\n pervious_owner\n purchase_price\n sale_price\n Vehicle_description ")
        if edit_info == 'Vehicle_make':
            my_value = input("how would you like to edit it?: ")
            my_db.executeQuery("UPDATE vehicle_info SET Vehicle_make = ("'+Vehicle_make+'") WHERE  Vehicle_make = ("'+my_value+'") ")
            my_result.conn.commit() 
        elif edit_info == 'Vehicle_Model':
            my_value = input("how would you like to edit it?: ")
            my_db.executeQuery("UPDATE vehicle_info SET Vehicle_Model = ("'+Vehicle_Model+'") WHERE  Vehicle_Model = ("'+my_value+'") ")
            my_result.conn.commit() 
        elif edit_info == 'VIN':
            my_value = input("how would you like to edit it?: ")
            my_db.executeQuery("UPDATE vehicle_info SET VIN = ("'+VIN+'") WHERE  VIN = ("'+my_value+'") ")
            my_result.conn.commit() 
        elif edit_info == 'pervious_owner':
            my_value = input("how would you like to edit it?: ")
            my_db.executeQuery("UPDATE vehicle_info SET pervious_owner = ("'+pervious_owner+'") WHERE  pervious_owner = ("'+my_value+'") ")
            my_result.conn.commit()
        elif edit_info == 'purchase_price':
            my_value = input("how would you like to edit it?: ")
            my_db.executeQuery("UPDATE vehicle_info SET purchase_price = ("'+purchase_price+'") WHERE  purchase_price = ("'+my_value+'") ")
            my_result.conn.commit() 
        elif edit_info == 'sale_price':
            my_value = input("how would you like to edit it?: ")
            my_db.executeQuery("UPDATE vehicle_info SET sale_price = ("'+sale_price+'") WHERE  sale_price = ("'+my_value+'") ")
            my_result.conn.commit() 
        elif edit_info == 'Vehicle_description':
            my_value = input("how would you like to edit it?: ")
            my_db.executeQuery("UPDATE vehicle_info SET Vehicle_description = ("'+Vehicle_description+'") WHERE  Vehicle_description= ("'+my_value+'") ")
            my_result.conn.commit() 
        else:
            vehicle_info = False
        
        
    elif user_choice =="4":
        delete_info = input("what would you like to delete?\n Vehicle_make\n Vehicle_Model\n VIN pervious_owner\n purchase_price\n sale_price\n Vehicle_description ")
        my_sql = "DELETE FROM vehicle_info WHERE %s = %s"
        if delete_info == 'Vehicle_make':
            my_value = input("what would you like to delete it to?: ")
            new_value = input("are you sure you want to delete" + my_value"? (Y/N) ")
            if new_value.lower() == "y":
                my_db.executeQuery("DELETE FROM vehicle_info WHERE Vehicle_make = ("'+my_value+'")")
                my_result.conn.commit() 
            else:
                break
        elif delete_info == 'Vehicle_Model':
            my_value = input("what would you like to delete it to?: ")
            new_value = input("are you sure you want to delete" + my_value"? (Y/N) ")
            if new_value.lower() == "y":
                my_db.executeQuery("DELETE FROM vehicle_info WHERE Vehicle_Model = ("'+my_value+'")")
                my_result.conn.commit() 
            else:
                break  
        elif delete_info == 'VIN':
            my_value = input("what would you like to delete it to?: ")
            new_value = input("are you sure you want to delete" + my_value"? (Y/N) ")
            if new_value.lower() == "y":
                my_db.executeQuery("DELETE FROM vehicle_info WHERE VIN = ("'+my_value+'")")
                my_result.conn.commit() 
            else:
                break  
        elif delete_info == 'pervious_owner':
            my_value = input("what would you like to delete it to?: ")
            new_value = input("are you sure you want to delete" + my_value"? (Y/N) ")
            if new_value.lower() == "y":
                my_db.executeQuery("DELETE FROM vehicle_info WHERE pervious_owner = ("'+my_value+'")")
                my_result.conn.commit() 
            else:
                break 
        elif delete_info == 'purchase_price':
            my_value = input("what would you like to delete it to?: ")
            new_value = input("are you sure you want to delete" + my_value"? (Y/N) ")
            if new_value.lower() == "y":
                my_db.executeQuery("DELETE FROM vehicle_info WHERE purchase_price = ("'+my_value+'")")
                my_result.conn.commit() 
            else:
                break 
        elif delete_info == 'sale_price':
            my_value = input("what would you like to delete it to?: ")
            new_value = input("are you sure you want to delete" + my_value"? (Y/N) ")
            if new_value.lower() == "y":
                my_db.executeQuery("DELETE FROM vehicle_info WHERE sale_price = ("'+my_value+'")")
                my_result.conn.commit() 
            else:
                break 
        elif delete_info == 'Vehicle_description':
            my_value = input("what would you like to delete it to?: ")
            new_value = input("are you sure you want to delete" + my_value"? (Y/N) ")
            if new_value.lower() == "y":
                my_db.executeQuery("DELETE FROM vehicle_info WHERE Vehicle_description = ("'+my_value+'")")
                my_result.conn.commit() 
            else:
                break 
        else:
            vehicle_info = False


    else user_choice =="5":
        print("Goodbye!!")
        break


# my_db.executeQuery("INSERT INTO  course_info (	course_discipline, 	course_num, course_title ) VALUES('IT', '650' , 'SOFTWARE PRINCIPLES')")

# my_db.executeQuery("UPDATE course_info SET letter_grade =  'A' , course_gpa = '3.7' WHERE course_id  = '2'")

# my_db.conn.commit()


# for record in my_result:
#     showall = input("Would you like to see all Vehicles? (Y/N) ")
#     if showall.lower() == "y":
#         print(my_result)
#     else:
#         break



# for record in my_result:
#     add_info = input("Would you like to add a vehicle? (Y/N) ")
#     if add_info.lower() == "y":
#         Vehicle_make = input("Vehicle make: ")
#         Vehicle_Model = input("Vehicle Model: ")
#         VIN = input("VIN: ")
#         pervious_owner = input("Previous Owner: ")
#         purchase_price = input("Purchased price: ")
#         sale_price = input("Sales Price: ")
#         Vehicle_description = input("Describe Vehicle: ")
#         my_db.executeQuery("INSERT INTO  course_info (Vehicle_make, Vehicle_Model, VIN, pervious_owner, purchase_price, sale_price, Vehicle_description)") #VALUES("Vehicle_make, Vehicle_Model, VIN, pervious_owner, purchase_price, sale_price, Vehicle_description ")")




Vehicle_make, Vehicle_Model, VIN, pervious_owner, purchase_price, sale_price, Vehicle_description 

    
 