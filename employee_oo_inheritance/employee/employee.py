class Employee(object):

    def __init__(self, fname, lname, no_years):
        self.fname = fname
        self.lname = lname
        self.no_years = no_years
    
    def calculate_salary(self):
        base_salary = 50000
        if self.no_years < 3:
            self.salary = base_salary * 1.01
        elif self.no_years <= 5:
            self.salary = base_salary * 1.10
        elif self.no_years > 5:
            self.salary = base_salary * 1.25
        return self.salary
            
    def get_details(self):
        self.calculate_salary()
        return "{0} {1}'s has been at the company for {2} years. His salary is {3}".format(self.fname, self.lname, self.no_years, self.salary)
        
class Developer(Employee):
    
    def __init__(self, fname, lname, no_years, lang):
        super(Developer, self).__init__(fname, lname, no_years)
        self.lang = lang
        
    def calculate_salary(self):
        salary = super(Developer, self).calculate_salary()
        if self.lang.lower() == "python":
            salary  = salary * 1.30
        elif self.lang.lower() == "javascript":
            salary = salary * 1.20
        elif self.lang.lower() == "html":
            salary = salary * 1.10
        return salary
        
    def get_details(self):
        salary = self.calculate_salary()
        return "{0} {1}'s has been at the company for {2} years working as a {3} developer. salary is {4}".format(self.fname, self.lname, self.no_years, self.lang, salary)
        
class SalesPerson(Employee):
    
    def __init__(self, fname, lname, no_years, territory):
        super(SalesPerson, self).__init__(fname, lname, no_years)
        self.territory = territory
        
    def calculate_salary(self):
        salary = super(SalesPerson, self).calculate_salary()
        if self.territory.lower() == "ireland":
            salary  = salary * 1.10
        elif self.territory.lower() == "uk":
            salary = salary * 1.20
        elif self.territory.lower() == "europe":
            salary = salary * 1.50
        return salary
        
    def get_details(self):
        salary = self.calculate_salary()
        return "{0} {1}'s has been at the company for {2} years working as a sales rep for  {3} . salary is {4}".format(self.fname, self.lname, self.no_years, self.territory, salary)
        
    