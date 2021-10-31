import math
import random


class EmployeeWageCalculation:
    """ class that represents employee wage calculation"""
    IS_ABSENT = 0
    IS_FULL_TIME = 1
    IS_PART_TIME = 2

    def __init__(self, company_name, employee_wage_per_hour, number_of_working_days,
                 maximum_hour_in_month):
        """ constructor to initialize instance variable"""
        self.company_name = company_name;
        self.employee_wage_per_hour = employee_wage_per_hour
        self.number_of_working_days = number_of_working_days
        self.maximum_hour_in_month = maximum_hour_in_month

    def compute_employee_wage(self):
        """ method to calculate employee total wage"""
        total_working_days = 0
        total_employee_hours = 0
        while total_working_days < self.number_of_working_days and total_employee_hours <= self.maximum_hour_in_month:
            employee_check = math.floor(random.random() * 10) % 3
            if employee_check == self.IS_FULL_TIME:
                employee_hour = 8
            elif employee_check == self.IS_PART_TIME:
                employee_hour = 4
            else:
                employee_hour = 0
            total_employee_hours = total_employee_hours + employee_hour
            total_working_days = total_working_days + 1
        total_employee_wage = total_employee_hours * self.employee_wage_per_hour
        print(self.company_name)
        print("Total Employee Wage :" + str(total_employee_wage))


employee_tcs = EmployeeWageCalculation("TCS", 20, 20, 100)
employee_tcs.compute_employee_wage()
employee_infosys = EmployeeWageCalculation("Infosys", 15, 18, 80)
employee_infosys.compute_employee_wage()
