import math
import random
IS_ABSENT = 0
IS_PRESENT = 1

employee_check = math.floor(random.random() * 10) % 2

if employee_check == IS_PRESENT:
    print("employee present")
else:
    print("employee absent")
