class ValueIsNegative(Exception):
    """Raised when the input value is negative"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ValueIsPositive(Exception):
    """Raised when the input value is positive"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


number = 0

try:
    i_num = int(input("Enter a number: "))
    if i_num < number:
        raise ValueIsNegative("This value is  small")
    elif i_num > number:
        raise ValueIsPositive("This value is  large")
except ValueIsNegative as e:
    print(e.__str__())
    print(ValueIsNegative.__doc__)
except ValueIsPositive as e:
    print(e.__str__())
    print(ValueIsPositive.__doc__)
finally:
    print("executes anyway")
