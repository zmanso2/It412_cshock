from person import Person
class student(Person):
    def _init_(self,passed_name, passed_id, passed_email, passed_program):
        super(). _init_ (passed_name, passed_id, passed_email)

        self.program = passed_program
    def displayinformation (self):
        print(self.name)
        print(self.program)