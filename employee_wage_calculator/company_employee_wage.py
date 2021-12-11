class CompanyEmployeeWage:
    """ class that represent employee wage description"""
    total_employee_wage = 0

    def __init__(self, company_name, employee_wage_per_hour, number_of_working_days,
                 maximum_hour_in_month):
        """ constructor to initialize instance variable"""
        self.company_name = company_name
        self.employee_wage_per_hour = employee_wage_per_hour
        self.number_of_working_days = number_of_working_days
        self.maximum_hour_in_month = maximum_hour_in_month

    def set_total_employee_wage(self, total_employee_wage):
        """ method to set total employee wage"""
        self.total_employee_wage = total_employee_wage

    def __str__(self):
        return "Total Employee Wage for Company " + str(self.company_name) + " is " + str(self.total_employee_wage)
