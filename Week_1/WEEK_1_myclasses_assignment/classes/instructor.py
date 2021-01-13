from person import Person

class instructor(Person):
    def _init_(self,passed_name, passed_id, passed_email, passed_degree, passed_insti):
        super(). _init_ (passed_name, passed_id, passed_email)
        self.insti = passed_insti
        self.degree = passed_degree