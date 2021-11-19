class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        self.empCount = 10

    def displayCount(self):
        return f"Total Employee {Employee.empCount} {self.empCount}"

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print
# "Total Employee %d" % Employee.empCount
print(emp1.displayCount())
print(emp2.displayCount())

# emp1.age = 7  # Add an 'age' attribute.
# emp1.age = 8  # Modify 'age' attribute.
# del emp1.age  # Delete 'age' attribute.
#
# hasattr(emp1, 'age')  # Returns true if 'age' attribute exists
# getattr(emp1, 'age')  # Returns value of 'age' attribute
# setattr(emp1, 'age', 8)  # Set attribute 'age' at 8
# delattr(emp1, 'age')  # Delete attribute 'age'
