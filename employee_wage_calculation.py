import math
import random

IS_ABSENT = 0
IS_FULL_TIME = 1
IS_PART_TIME = 2

EMPLOYEE_WAGE_PER_HOUR = 20
NUMBER_OF_WORKING_DAYS = 20
employee_hour = 0
total_employee_wage = 0


for i in range(NUMBER_OF_WORKING_DAYS):
    print(i)
    employee_check = math.floor(random.random() * 10) % 3
    if employee_check == IS_FULL_TIME:
        employee_hour = 8
    elif employee_check == IS_PART_TIME:
        employee_hour = 4
    else:
        employee_hour = 0
    employee_wage = employee_hour * EMPLOYEE_WAGE_PER_HOUR
    total_employee_wage = total_employee_wage + employee_wage

print(" Total Employee Wage :" + str(total_employee_wage))
