import math
from company_employee_wage import CompanyEmployeeWage
import random


class EmployeeWageCalculation:
    """ class that represents employee wage calculation"""
    IS_ABSENT = 0
    IS_FULL_TIME = 1
    IS_PART_TIME = 2
    company_employee_wage_list = []

    def add_company_employee_wage(self, company_name, wage_per_hour, no_of_days, max_hours_per_month):
        self.company_employee_wage_list.append(
            CompanyEmployeeWage(company_name, wage_per_hour, no_of_days, max_hours_per_month))

    def calculate_company_employee_wage(self):
        for i in range(len(self.company_employee_wage_list)):
            self.company_employee_wage_list[i].set_total_employee_wage(
                self.calculate_employee_wage(self.company_employee_wage_list[i]))
            print(self.company_employee_wage_list[i])

    def calculate_employee_wage(self, employee):
        """ method to calculate employee total wage"""
        total_employee_hours = 0
        total_working_days = 0
        while total_employee_hours < employee.maximum_hour_in_month and \
                total_working_days < employee.number_of_working_days:

            employee_check = math.floor(random.random() * 10) % 3
            if employee_check == self.IS_FULL_TIME:
                employee_hour = 8
            elif employee_check == self.IS_PART_TIME:
                employee_hour = 4
            else:
                employee_hour = 0
            total_employee_hours = total_employee_hours + employee_hour
            total_working_days = total_working_days + 1
        print(employee.company_name)
        print("Total Employee Wage :{0}".format(
            str(total_employee_hours * employee.employee_wage_per_hour)))
        return total_employee_hours * employee.employee_wage_per_hour


employee = EmployeeWageCalculation()
employee.add_company_employee_wage("TCS", 20, 6, 10)
employee.add_company_employee_wage("WIPRO", 10, 5, 20)
employee.add_company_employee_wage("INFOSYS", 10, 5, 20)
employee.calculate_company_employee_wage()
