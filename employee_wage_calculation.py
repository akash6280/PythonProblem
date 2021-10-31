import math
import random

IS_ABSENT = 0
IS_FULL_TIME = 1
IS_PART_TIME = 2

EMPLOYEE_WAGE_PER_HOUR = 20
employee_hour = 0
employee_check = math.floor(random.random() * 10) % 3

if employee_check == IS_FULL_TIME:
    employee_hour = 8
elif employee_check == IS_PART_TIME:
    employee_hour = 4
else:
    employee_hour = 0

employee_wage = employee_hour * EMPLOYEE_WAGE_PER_HOUR
print("Employee Wage :" + str(employee_wage))
