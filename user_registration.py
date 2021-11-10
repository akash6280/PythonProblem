import re


class UserRegistration():
    def __init__(self):
        pass

    @staticmethod
    def validate_first_name(name_to_be_validated):
        pattern = "^[A-Z][A-Za-z]{2,}$"
        result = re.match(pattern, name_to_be_validated)
        if result:
            print("first name is valid")
        else:
            print("first name is not valid")

    @staticmethod
    def validate_last_name(name_to_be_validated):
        pattern = "^[A-Z][A-Za-z]{2,}$"
        result = re.match(pattern, name_to_be_validated)
        if result:
            print("last name is valid")
        else:
            print("last name is not valid")


if __name__ == "__main__":
    first_name = input("enter name to be checked ")
    UserRegistration.validate_first_name(first_name)

    last_name = input("enter name to be checked ")
    UserRegistration.validate_last_name(last_name)


