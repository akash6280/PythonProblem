import math
import random

IS_ABSENT = 0
IS_PRESENT = 1
EMPLOYEE_WAGE_PER_HOUR = 20
employee_hour = 0
employee_check = math.floor(random.random() * 10) % 2

if employee_check == IS_PRESENT:
    print("employee present")
    employee_hour = 8
else:
    print("employee absent")
    employee_hour = 0

employee_wage = employee_hour * EMPLOYEE_WAGE_PER_HOUR
print("Employee Wage :"+str(employee_wage))
