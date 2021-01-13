from person import Person
from student import student
from instructor import instructor

class vaildator():
    def _init_(self):
        self.badchars = [ "!", '"', "@", "#", "$", "^","&","*","(",")", "-", "_", ",", "<",">","?","?",";",":", "[","]", "{","}"," \\"," /"]
    def isvalidtype(self, passed_type):
        if passed_type.lower() == "s" or passed_type.lower == "i":
            return True
        else:
            print ( " please type user type!")
            
            return False
    
    def isvalidname(self, passed_type):
        if(passed_name):
            for character in passed_name:
                if character is self.badchars or character.isdigit():
                    bad_char_found = True
                    
                    break
                    if bad_char_found:
                        print("wrong char")
                        return False
                    else:
                        return True
                else:
                    print("please enter in name")
                    return False
    def isvalidprogram(self, passed_type):
        if(passed_program):
            return True
        else:
            print("please enter in name")
            return False

my_validator = validator()
