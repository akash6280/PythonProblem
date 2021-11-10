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

    @staticmethod
    def validate_email(email_to_be_validated):
        pattern = "^[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]([+-_.][a-zA-Z]*)?@[a-zA-Z0-9]*[.][a-z]{2,4}([.][a-zA-z]{2})?$"
        result = re.match(pattern, email_to_be_validated)
        if result:
            print("email is valid")
        else:
            print("email is not valid")

    @staticmethod
    def validate_phone(phone_to_be_validated):
        pattern = "^[0-9]{2}[ ][1-9][0-9]{9}$"
        result = re.match(pattern, phone_to_be_validated)
        if result:
            print("phone number is valid")
        else:
            print("phone number is not valid")


if __name__ == "__main__":
    first_name = input("enter first name to be checked ")
    UserRegistration.validate_first_name(first_name)

    last_name = input("enter last name to be checked ")
    UserRegistration.validate_last_name(last_name)

    email_id = input("enter email to be checked ")
    UserRegistration.validate_email(email_id)

    phone_number = input("enter phone to be checked ")
    UserRegistration.validate_phone(phone_number)


