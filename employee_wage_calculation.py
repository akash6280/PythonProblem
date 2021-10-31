import math
import random

IS_ABSENT = 0
IS_FULL_TIME = 1
IS_PART_TIME = 2

EMPLOYEE_WAGE_PER_HOUR = 20
NUMBER_OF_WORKING_DAYS = 20
MAXIMUM_HOURS_IN_MONTH = 100
employee_hour = 0
total_employee_wage = 0
total_working_days = 0
total_employee_hours = 0

while total_working_days < NUMBER_OF_WORKING_DAYS and total_employee_hours <= MAXIMUM_HOURS_IN_MONTH:
    
    employee_check = math.floor(random.random() * 10) % 3
    if employee_check == IS_FULL_TIME:
        employee_hour = 8
    elif employee_check == IS_PART_TIME:
        employee_hour = 4
    else:
        employee_hour = 0
    total_employee_hours += employee_hour
    total_working_days = total_working_days + 1

total_employee_wage = total_employee_hours * EMPLOYEE_WAGE_PER_HOUR
print(" Total Employee Wage :" + str(total_employee_wage))
