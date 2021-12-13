import pytest
from user_registration import UserRegistration
from user_registration_exception import UserRegistrationException

user_registration = UserRegistration()
list_of_emails = [("abc@yahoo.com", True), ("abc-100@yahoo.com", True), ("abc.100@yahoo.com", True),
                  ("abc111@abc.com", True), ("abc-100@abc.net", True), ("abc.100@abc.com.au", True),
                  ("abc@1.com", True),
                  ("abc@gmail.com.com", True), ("abc+100@gmail.com", True), (".abc@abc.com", False),
                  ("abc@123@gmaila", False),
                  ("abc@abc@gmailcom", False),
                  ("abc123@gmaila", False), ("abc..2002@gmail.com", False), ("abc@abc@gmail.com", False),
                  ("abc()*@gmail.com", False), ("abc@%*@gmail.com", False),
                  ("abc@gmail.com.1a", False), ("abc@gmail.com.aa.au", False)]


@pytest.mark.parametrize("email,expected", list_of_emails)
def test_email(email, expected):
    assert user_registration.validate_email(email) == expected


def test_first_name_with_proper_format():
    assert user_registration.validate_first_name("Akash")


@pytest.mark.xfail
def test_first_name_with_incorrect_format():
    assert user_registration.validate_first_name("akash")


def test_last_name_with_proper_format():
    assert user_registration.validate_first_name("Singh")


@pytest.mark.xfail
def test_last_name_with_incorrect_format():
    assert user_registration.validate_first_name("singh")


def test_mobile_number_with_correct_pattern():
    assert user_registration.validate_phone("91 8090433565")


@pytest.mark.xfail
def test_mobile_number_with_incorrrect_pattern():
    assert user_registration.validate_phone("80904335")


def test_password():
    assert user_registration.validate_password("Akash@123")


@pytest.mark.xfail
def test_password_wrong_input_pattern():
    assert user_registration.validate_password("Akash")
